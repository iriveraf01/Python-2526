from calendar import monthrange
from datetime import date, datetime, time, timedelta
import sys
from functools import wraps

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for,
)
from mysql.connector import Error

sys.path.append("scripts")
from conexion import cerrar_conexion, obtener_conexion


app = Flask(__name__, template_folder="html", static_folder=".")
app.secret_key = "super_secret_dentify_key"

DIAS_SEMANA = {
    0: "LUNES",
    1: "MARTES",
    2: "MIERCOLES",
    3: "JUEVES",
    4: "VIERNES",
    5: "SABADO",
    6: "DOMINGO",
}

MESES = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre",
}


def get_connection():
    return obtener_conexion()


def fetch_one(query, params=()):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params)
        return cursor.fetchone()
    finally:
        cerrar_conexion(conn)


def fetch_all(query, params=()):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params)
        return cursor.fetchall()
    finally:
        cerrar_conexion(conn)


def execute(query, params=()):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.lastrowid
    except Exception:
        conn.rollback()
        raise
    finally:
        cerrar_conexion(conn)


def login_required(*roles):
    def decorator(view):
        @wraps(view)
        def wrapper(*args, **kwargs):
            rol = session.get("rol")
            if not rol:
                return redirect(url_for("login"))
            if roles and rol not in roles:
                flash("No tienes permiso para acceder a esa zona.", "error")
                return redirect(url_for("login"))
            return view(*args, **kwargs)

        return wrapper

    return decorator


def current_user_id():
    return session.get("user_id")


def get_role_id(nombre):
    role = fetch_one("SELECT id FROM roles WHERE nombre = %s", (nombre,))
    return role["id"] if role else None


def get_paciente_by_user(usuario_id):
    return fetch_one("SELECT * FROM pacientes WHERE usuario_id = %s", (usuario_id,))


def get_medico_by_user(usuario_id):
    return fetch_one("SELECT * FROM medicos WHERE usuario_id = %s", (usuario_id,))


def get_current_user():
    usuario_id = current_user_id()
    if not usuario_id:
        return None
    return fetch_one(
        "SELECT u.*, r.nombre AS rol_nombre "
        "FROM usuarios u JOIN roles r ON r.id = u.rol_id "
        "WHERE u.id = %s",
        (usuario_id,),
    )


def panel_url_for_role(rol):
    if rol == "ADMIN":
        return url_for("admin")
    if rol == "MEDICO":
        return url_for("doctor")
    if rol == "CLIENTE":
        return url_for("cliente")
    return url_for("index")


def as_time(value):
    if isinstance(value, timedelta):
        total = int(value.total_seconds())
        return time(total // 3600, (total % 3600) // 60)
    return value


def to_minutes(value):
    value = as_time(value)
    return value.hour * 60 + value.minute


def minutes_to_hora(minutes):
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def format_nombre(nombre, apellidos=None):
    return f"{nombre or ''} {apellidos or ''}".strip()


def add_months(value, amount):
    month_index = value.month - 1 + amount
    year = value.year + month_index // 12
    month = month_index % 12 + 1
    return date(year, month, 1)


@app.template_filter("hora")
def hora_filter(value):
    if value is None:
        return ""
    value = as_time(value)
    return value.strftime("%H:%M")


@app.template_filter("fecha")
def fecha_filter(value):
    if value is None:
        return ""
    if isinstance(value, datetime):
        value = value.date()
    return value.strftime("%d/%m/%Y")


@app.template_filter("dinero")
def dinero_filter(value):
    if value is None:
        return ""
    return f"{float(value):.2f} €"


@app.context_processor
def inject_globals():
    return {
        "usuario_nombre": session.get("nombre"),
        "usuario_rol": session.get("rol"),
        "today": date.today().isoformat(),
    }


@app.after_request
def disable_cache(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("js", path)


@app.route("/")
def index():
    servicios = fetch_all(
        "SELECT nombre, descripcion, precio, duracion_minutos FROM servicios "
        "WHERE activo = 1 ORDER BY precio LIMIT 6"
    )
    medicos = fetch_all(
        "SELECT u.nombre, u.apellidos, m.especialidad, m.descripcion "
        "FROM medicos m JOIN usuarios u ON u.id = m.usuario_id "
        "ORDER BY u.nombre"
    )
    user = get_current_user()
    show_role_modal = bool(session.pop("show_role_modal", False))
    return render_template(
        "index.html",
        servicios=servicios,
        medicos=medicos,
        user=user,
        panel_url=panel_url_for_role(user["rol_nombre"]) if user else None,
        show_role_modal=show_role_modal,
    )


@app.route("/login.html", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = fetch_one(
            "SELECT u.*, r.nombre AS rol_nombre "
            "FROM usuarios u JOIN roles r ON u.rol_id = r.id "
            "WHERE u.email = %s AND u.password = %s AND u.activo = 1",
            (email, password),
        )

        if user:
            session.clear()
            session["user_id"] = user["id"]
            session["rol"] = user["rol_nombre"]
            session["nombre"] = format_nombre(user["nombre"], user["apellidos"])
            session["show_role_modal"] = True

            return redirect(url_for("index"))

        flash("Correo o contraseña incorrectos.", "error")

    return render_template("login.html")


@app.route("/registro.html", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form.get("name", "").strip()
        apellidos = request.form.get("apellidos", "").strip()
        email = request.form.get("email", "").strip().lower()
        telefono = request.form.get("telefono", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not nombre or not email or not password:
            flash("Rellena nombre, correo y contraseña.", "error")
            return render_template("registro.html")
        if password != confirm_password:
            flash("Las contraseñas no coinciden.", "error")
            return render_template("registro.html")
        if fetch_one("SELECT id FROM usuarios WHERE email = %s", (email,)):
            flash("Ya existe una cuenta con ese correo.", "error")
            return render_template("registro.html")

        cliente_role = get_role_id("CLIENTE")
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, apellidos, email, password, telefono, rol_id) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (nombre, apellidos or None, email, password, telefono or None, cliente_role),
            )
            usuario_id = cursor.lastrowid
            cursor.execute(
                "INSERT INTO pacientes (usuario_id, observaciones) VALUES (%s, %s)",
                (usuario_id, "Paciente registrado desde la web"),
            )
            conn.commit()
            flash("Registro completado. Ya puedes iniciar sesión.", "success")
            return redirect(url_for("login"))
        except Error as exc:
            conn.rollback()
            flash(f"No se pudo completar el registro: {exc}", "error")
        finally:
            cerrar_conexion(conn)

    return render_template("registro.html")


@app.route("/panel")
@login_required("ADMIN", "MEDICO", "CLIENTE")
def panel():
    return redirect(panel_url_for_role(session.get("rol")))


@app.route("/perfil.html")
@login_required("ADMIN", "MEDICO", "CLIENTE")
def perfil():
    user = get_current_user()
    paciente = get_paciente_by_user(user["id"]) if user["rol_nombre"] == "CLIENTE" else None
    medico = get_medico_by_user(user["id"]) if user["rol_nombre"] == "MEDICO" else None
    stats = {}
    if user["rol_nombre"] == "CLIENTE" and paciente:
        stats["citas"] = fetch_one("SELECT COUNT(*) AS total FROM citas WHERE paciente_id = %s", (paciente["id"],))["total"]
        stats["futuras"] = fetch_one(
            "SELECT COUNT(*) AS total FROM citas WHERE paciente_id = %s AND fecha >= CURDATE() "
            "AND estado IN ('PENDIENTE', 'ACEPTADA')",
            (paciente["id"],),
        )["total"]
    elif user["rol_nombre"] == "MEDICO" and medico:
        stats["citas"] = fetch_one("SELECT COUNT(*) AS total FROM citas WHERE medico_id = %s", (medico["id"],))["total"]
        stats["futuras"] = fetch_one(
            "SELECT COUNT(*) AS total FROM citas WHERE medico_id = %s AND fecha >= CURDATE() "
            "AND estado IN ('PENDIENTE', 'ACEPTADA')",
            (medico["id"],),
        )["total"]
    elif user["rol_nombre"] == "ADMIN":
        stats["citas"] = fetch_one("SELECT COUNT(*) AS total FROM citas")["total"]
        stats["futuras"] = fetch_one(
            "SELECT COUNT(*) AS total FROM citas WHERE fecha >= CURDATE() AND estado IN ('PENDIENTE', 'ACEPTADA')"
        )["total"]

    return render_template(
        "perfil.html",
        user=user,
        paciente=paciente,
        medico=medico,
        stats=stats,
        panel_url=panel_url_for_role(user["rol_nombre"]),
    )


def appointment_query(where="", order="c.fecha ASC, c.hora_inicio ASC"):
    return (
        "SELECT c.*, "
        "up.nombre AS paciente_nombre, up.apellidos AS paciente_apellidos, "
        "up.email AS paciente_email, up.telefono AS paciente_telefono, "
        "um.nombre AS medico_nombre, um.apellidos AS medico_apellidos, "
        "m.especialidad, s.nombre AS servicio_nombre, s.precio, s.duracion_minutos "
        "FROM citas c "
        "JOIN pacientes p ON p.id = c.paciente_id "
        "JOIN usuarios up ON up.id = p.usuario_id "
        "JOIN medicos m ON m.id = c.medico_id "
        "JOIN usuarios um ON um.id = m.usuario_id "
        "JOIN servicios s ON s.id = c.servicio_id "
        f"{where} ORDER BY {order}"
    )


def get_available_slots(fecha_text, medico_id, servicio_id):
    try:
        selected_date = datetime.strptime(fecha_text, "%Y-%m-%d").date()
    except ValueError:
        selected_date = date.today()

    servicio = fetch_one(
        "SELECT id, nombre, duracion_minutos FROM servicios WHERE id = %s AND activo = 1",
        (servicio_id,),
    )
    if not servicio:
        return selected_date, []

    horario = fetch_one(
        "SELECT hora_inicio, hora_fin FROM horarios_medicos "
        "WHERE medico_id = %s AND dia_semana = %s AND activo = 1",
        (medico_id, DIAS_SEMANA[selected_date.weekday()]),
    )
    if not horario:
        return selected_date, []

    reservas = fetch_all(
        "SELECT hora_inicio, hora_fin FROM citas "
        "WHERE medico_id = %s AND fecha = %s AND estado IN ('PENDIENTE', 'ACEPTADA')",
        (medico_id, selected_date),
    )
    ocupadas = [(to_minutes(r["hora_inicio"]), to_minutes(r["hora_fin"])) for r in reservas]

    duracion = int(servicio["duracion_minutos"])
    inicio = to_minutes(horario["hora_inicio"])
    fin = to_minutes(horario["hora_fin"])
    ahora = datetime.now()
    slots = []

    current = inicio
    while current + duracion <= fin:
        slot_fin = current + duracion
        ocupado = any(current < ocupado_fin and slot_fin > ocupado_inicio for ocupado_inicio, ocupado_fin in ocupadas)
        en_pasado = selected_date < date.today() or (
            selected_date == date.today() and current <= ahora.hour * 60 + ahora.minute
        )
        if not ocupado and not en_pasado:
            slots.append({"inicio": minutes_to_hora(current), "fin": minutes_to_hora(slot_fin)})
        current += 15

    return selected_date, slots


def build_calendar_days(reference_date, medico_id, servicio_id):
    first_day = date(reference_date.year, reference_date.month, 1)
    total_days = monthrange(reference_date.year, reference_date.month)[1]
    days = [{"empty": True} for _ in range(first_day.weekday())]

    for day_number in range(1, total_days + 1):
        day = date(reference_date.year, reference_date.month, day_number)
        _, slots = get_available_slots(day.isoformat(), medico_id, servicio_id)
        days.append(
            {
                "empty": False,
                "date": day,
                "day": day_number,
                "available": len(slots),
                "selected": day == reference_date,
                "past": day < date.today(),
            }
        )

    while len(days) % 7 != 0:
        days.append({"empty": True})

    return days


@app.route("/admin.html")
@login_required("ADMIN")
def admin():
    vista = request.args.get("vista", "mes")
    stats = {
        "total": fetch_one("SELECT COUNT(*) AS total FROM citas")["total"],
        "futuras": fetch_one(
            "SELECT COUNT(*) AS total FROM citas WHERE fecha >= CURDATE() "
            "AND estado IN ('PENDIENTE', 'ACEPTADA')"
        )["total"],
        "pendientes": fetch_one("SELECT COUNT(*) AS total FROM citas WHERE estado = 'PENDIENTE'")["total"],
        "aceptadas": fetch_one("SELECT COUNT(*) AS total FROM citas WHERE estado = 'ACEPTADA'")["total"],
    }
    caja = {
        "confirmado": fetch_one(
            "SELECT COALESCE(SUM(s.precio), 0) AS total "
            "FROM citas c JOIN servicios s ON s.id = c.servicio_id "
            "WHERE c.estado IN ('ACEPTADA', 'COMPLETADA')"
        )["total"],
        "pendiente": fetch_one(
            "SELECT COALESCE(SUM(s.precio), 0) AS total "
            "FROM citas c JOIN servicios s ON s.id = c.servicio_id "
            "WHERE c.estado = 'PENDIENTE'"
        )["total"],
        "mes_actual": fetch_one(
            "SELECT COALESCE(SUM(s.precio), 0) AS total "
            "FROM citas c JOIN servicios s ON s.id = c.servicio_id "
            "WHERE c.estado IN ('ACEPTADA', 'COMPLETADA') "
            "AND YEAR(c.fecha) = YEAR(CURDATE()) AND MONTH(c.fecha) = MONTH(CURDATE())"
        )["total"],
    }
    ingresos_por_servicio = fetch_all(
        "SELECT s.nombre, COUNT(c.id) AS reservas, COALESCE(SUM(s.precio), 0) AS total "
        "FROM servicios s "
        "LEFT JOIN citas c ON c.servicio_id = s.id AND c.estado IN ('ACEPTADA', 'COMPLETADA') "
        "WHERE s.activo = 1 "
        "GROUP BY s.id, s.nombre "
        "ORDER BY total DESC, reservas DESC, s.nombre ASC"
    )
    ingresos_recientes = fetch_all(
        appointment_query(
            "WHERE c.estado IN ('ACEPTADA', 'COMPLETADA')",
            "c.fecha DESC, c.hora_inicio DESC",
        )
    )
    citas = fetch_all(appointment_query("WHERE c.fecha >= CURDATE()"))
    pendientes = fetch_all(appointment_query("WHERE c.estado = 'PENDIENTE'"))
    return render_template(
        "admin.html",
        stats=stats,
        caja=caja,
        ingresos_por_servicio=ingresos_por_servicio,
        ingresos_recientes=ingresos_recientes,
        citas=citas,
        pendientes=pendientes,
        vista=vista,
    )


@app.post("/admin/citas/<int:cita_id>/<accion>")
@login_required("ADMIN")
def admin_cambiar_cita(cita_id, accion):
    estados = {"aceptar": "ACEPTADA", "rechazar": "RECHAZADA"}
    if accion not in estados:
        flash("Acción no válida.", "error")
        return redirect(url_for("admin"))

    execute("UPDATE citas SET estado = %s WHERE id = %s", (estados[accion], cita_id))
    flash(f"Cita {estados[accion].lower()} correctamente.", "success")
    return redirect(url_for("admin"))


@app.route("/cliente.html")
@login_required("CLIENTE")
def cliente():
    paciente = get_paciente_by_user(current_user_id())
    if not paciente:
        flash("Tu usuario no tiene ficha de paciente. Contacta con administración.", "error")
        return redirect(url_for("logout"))

    servicios = fetch_all("SELECT * FROM servicios WHERE activo = 1 ORDER BY nombre")
    medicos = fetch_all(
        "SELECT m.*, u.nombre, u.apellidos FROM medicos m JOIN usuarios u ON u.id = m.usuario_id ORDER BY u.nombre"
    )
    servicio_id = int(request.args.get("servicio_id") or servicios[0]["id"])
    medico_id = int(request.args.get("medico_id") or medicos[0]["id"])
    fecha_text = request.args.get("fecha") or date.today().isoformat()
    fecha_seleccionada, slots = get_available_slots(fecha_text, medico_id, servicio_id)
    servicio_seleccionado = next((servicio for servicio in servicios if servicio["id"] == servicio_id), servicios[0])
    mes_anterior = add_months(fecha_seleccionada, -1)
    mes_siguiente = add_months(fecha_seleccionada, 1)
    calendar_days = build_calendar_days(fecha_seleccionada, medico_id, servicio_id)

    proximas = fetch_all(
        appointment_query(
            "WHERE c.paciente_id = %s AND c.fecha >= CURDATE() "
            "AND c.estado IN ('PENDIENTE', 'ACEPTADA')"
        ),
        (paciente["id"],),
    )
    historial = fetch_all(
        appointment_query("WHERE c.paciente_id = %s", "c.fecha DESC, c.hora_inicio DESC"),
        (paciente["id"],),
    )
    return render_template(
        "cliente.html",
        paciente=paciente,
        servicios=servicios,
        medicos=medicos,
        servicio_id=servicio_id,
        medico_id=medico_id,
        servicio_seleccionado=servicio_seleccionado,
        fecha_seleccionada=fecha_seleccionada,
        calendar_days=calendar_days,
        mes_label=f"{MESES[fecha_seleccionada.month].capitalize()} {fecha_seleccionada.year}",
        mes_anterior=mes_anterior,
        mes_siguiente=mes_siguiente,
        slots=slots,
        proximas=proximas,
        historial=historial,
    )


@app.post("/cliente/reservar")
@login_required("CLIENTE")
def cliente_reservar():
    paciente = get_paciente_by_user(current_user_id())
    servicio_id = int(request.form.get("servicio_id"))
    medico_id = int(request.form.get("medico_id"))
    fecha_text = request.form.get("fecha")
    hora_inicio = request.form.get("hora_inicio")
    motivo = request.form.get("motivo", "").strip()

    selected_date, slots = get_available_slots(fecha_text, medico_id, servicio_id)
    slot = next((item for item in slots if item["inicio"] == hora_inicio), None)
    servicio = fetch_one("SELECT nombre FROM servicios WHERE id = %s", (servicio_id,))
    if not slot or not servicio:
        flash("Ese horario ya no está disponible. Elige otro hueco.", "error")
        return redirect(url_for("cliente", fecha=fecha_text, medico_id=medico_id, servicio_id=servicio_id))

    execute(
        "INSERT INTO citas (paciente_id, medico_id, servicio_id, fecha, hora_inicio, hora_fin, estado, motivo) "
        "VALUES (%s, %s, %s, %s, %s, %s, 'PENDIENTE', %s)",
        (
            paciente["id"],
            medico_id,
            servicio_id,
            selected_date,
            slot["inicio"],
            slot["fin"],
            motivo or servicio["nombre"],
        ),
    )
    flash("Solicitud de cita enviada. Administración la revisará.", "success")
    return redirect(url_for("cliente", fecha=fecha_text, medico_id=medico_id, servicio_id=servicio_id))


@app.post("/cliente/citas/<int:cita_id>/cancelar")
@login_required("CLIENTE")
def cliente_cancelar(cita_id):
    paciente = get_paciente_by_user(current_user_id())
    execute(
        "UPDATE citas SET estado = 'CANCELADA' "
        "WHERE id = %s AND paciente_id = %s AND estado IN ('PENDIENTE', 'ACEPTADA')",
        (cita_id, paciente["id"]),
    )
    flash("Cita cancelada.", "success")
    return redirect(url_for("cliente"))


@app.route("/doctor.html")
@login_required("MEDICO")
def doctor():
    medico = get_medico_by_user(current_user_id())
    if not medico:
        flash("Tu usuario no tiene ficha de médico. Contacta con administración.", "error")
        return redirect(url_for("logout"))

    fecha_text = request.args.get("fecha") or date.today().isoformat()
    try:
        fecha_seleccionada = datetime.strptime(fecha_text, "%Y-%m-%d").date()
    except ValueError:
        fecha_seleccionada = date.today()

    citas = fetch_all(
        appointment_query(
            "WHERE c.medico_id = %s AND c.fecha = %s "
            "AND c.estado IN ('ACEPTADA', 'PENDIENTE', 'COMPLETADA', 'NO_ASISTIO')"
        ),
        (medico["id"], fecha_seleccionada),
    )
    pacientes_ids = sorted({cita["paciente_id"] for cita in citas})
    historiales = {}
    if pacientes_ids:
        placeholders = ",".join(["%s"] * len(pacientes_ids))
        rows = fetch_all(
            "SELECT h.*, u.nombre AS medico_nombre, u.apellidos AS medico_apellidos "
            "FROM historial_pacientes h "
            "JOIN medicos m ON m.id = h.medico_id "
            "JOIN usuarios u ON u.id = m.usuario_id "
            f"WHERE h.paciente_id IN ({placeholders}) ORDER BY h.fecha DESC",
            tuple(pacientes_ids),
        )
        for row in rows:
            historiales.setdefault(row["paciente_id"], []).append(row)

    stats = {
        "hoy": fetch_one(
            "SELECT COUNT(*) AS total FROM citas WHERE medico_id = %s AND fecha = %s",
            (medico["id"], date.today()),
        )["total"],
        "del_dia": fetch_one(
            "SELECT COUNT(*) AS total FROM citas WHERE medico_id = %s AND fecha = %s "
            "AND estado IN ('ACEPTADA', 'PENDIENTE', 'COMPLETADA', 'NO_ASISTIO')",
            (medico["id"], fecha_seleccionada),
        )["total"],
        "por_confirmar": fetch_one(
            "SELECT COUNT(*) AS total FROM citas WHERE medico_id = %s AND fecha = %s AND estado = 'ACEPTADA'",
            (medico["id"], fecha_seleccionada),
        )["total"],
        "cerradas_dia": fetch_one(
            "SELECT COUNT(*) AS total FROM citas WHERE medico_id = %s AND fecha = %s "
            "AND estado IN ('COMPLETADA', 'NO_ASISTIO')",
            (medico["id"], fecha_seleccionada),
        )["total"],
        "completadas": fetch_one(
            "SELECT COUNT(*) AS total FROM citas WHERE medico_id = %s AND estado = 'COMPLETADA'",
            (medico["id"],),
        )["total"],
        "no_asistio": fetch_one(
            "SELECT COUNT(*) AS total FROM citas WHERE medico_id = %s AND estado = 'NO_ASISTIO'",
            (medico["id"],),
        )["total"],
    }
    return render_template(
        "doctor.html",
        medico=medico,
        citas=citas,
        citas_activas=[cita for cita in citas if cita["estado"] in ("ACEPTADA", "PENDIENTE")],
        citas_cerradas=[cita for cita in citas if cita["estado"] in ("COMPLETADA", "NO_ASISTIO")],
        historiales=historiales,
        stats=stats,
        fecha_seleccionada=fecha_seleccionada,
    )


@app.post("/doctor/citas/<int:cita_id>/asistencia")
@login_required("MEDICO")
def doctor_asistencia(cita_id):
    medico = get_medico_by_user(current_user_id())
    estado = request.form.get("estado")
    notas = request.form.get("notas_medico", "").strip()
    if estado not in {"COMPLETADA", "NO_ASISTIO"}:
        flash("Estado de asistencia no válido.", "error")
        return redirect(url_for("doctor"))

    cita = fetch_one(appointment_query("WHERE c.id = %s AND c.medico_id = %s"), (cita_id, medico["id"]))
    if not cita:
        flash("No se encontró esa cita en tu agenda.", "error")
        return redirect(url_for("doctor"))
    if cita["estado"] != "ACEPTADA":
        flash("Solo puedes confirmar asistencia en citas aceptadas y todavía abiertas.", "error")
        return redirect(url_for("doctor", fecha=cita["fecha"].isoformat()))

    execute(
        "UPDATE citas SET estado = %s, notas_medico = %s WHERE id = %s AND medico_id = %s AND estado = 'ACEPTADA'",
        (estado, notas or None, cita_id, medico["id"]),
    )
    if estado == "COMPLETADA":
        descripcion = f"{cita['servicio_nombre']} completado el {cita['fecha'].strftime('%d/%m/%Y')}."
        historial = fetch_one("SELECT id FROM historial_pacientes WHERE cita_id = %s", (cita_id,))
        if historial:
            execute(
                "UPDATE historial_pacientes SET descripcion = %s, tratamiento = %s WHERE id = %s",
                (descripcion, notas or cita["motivo"], historial["id"]),
            )
        else:
            execute(
                "INSERT INTO historial_pacientes (paciente_id, medico_id, cita_id, descripcion, tratamiento) "
                "VALUES (%s, %s, %s, %s, %s)",
                (cita["paciente_id"], medico["id"], cita_id, descripcion, notas or cita["motivo"]),
            )

    flash("Asistencia actualizada.", "success")
    return redirect(url_for("doctor", fecha=cita["fecha"].isoformat()))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True, use_reloader=False)
