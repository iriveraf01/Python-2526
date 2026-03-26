const API_URL = "http://127.0.0.1:8001";

let todasLasPlantas = [];
let plantaEditandoId = null;

export function inicializarInventario() {
  cargarPlantas();
  inicializarEventosInventario();
}

function inicializarEventosInventario() {
  const botonGuardar = document.querySelector("#guardarPlanta");
  const botonTodas = document.querySelectorAll(".btn-group .btn")[0];
  const botonSinUbicacion = document.querySelectorAll(".btn-group .btn")[1];

  if (botonGuardar) {
    botonGuardar.addEventListener("click", guardarPlanta);
  }

  if (botonTodas) {
    botonTodas.addEventListener("click", () => {
      activarFiltro(botonTodas);
      renderizarPlantas(todasLasPlantas);
    });
  }

  if (botonSinUbicacion) {
    botonSinUbicacion.addEventListener("click", () => {
      activarFiltro(botonSinUbicacion);
      const filtradas = todasLasPlantas.filter(
        (planta) => !planta.recinto_id || planta.recinto_id === "-- Sin asignar --"
      );
      renderizarPlantas(filtradas);
    });
  }
}

function activarFiltro(botonActivo) {
  document.querySelectorAll(".btn-group .btn").forEach((btn) => {
    btn.classList.remove("active");
  });
  botonActivo.classList.add("active");
}

async function cargarPlantas() {
  try {
    const response = await fetch(`${API_URL}/plantas`);
    if (!response.ok) throw new Error(`Error ${response.status}`);

    const plantas = await response.json();
    todasLasPlantas = plantas;

    renderizarPlantas(plantas);
  } catch (error) {
    console.error("Error al cargar plantas:", error);
  }
}

function renderizarPlantas(plantas) {
  const temp = document.querySelector("#templateTarjetaPlanta");
  const contenedor = document.querySelector(".contenedorTarjetas");

  contenedor.innerHTML = "";

  if (!plantas || plantas.length === 0) {
    contenedor.innerHTML = `
      <p class="text-body-secondary text-center mt-4">
        No hay plantas en el inventario
      </p>
    `;
    return;
  }

  plantas.forEach((planta) => {
    const clon = temp.content.cloneNode(true);

    clon.querySelector(".planta-nombre").textContent =
      planta.nombre || "Sin nombre";

    clon.querySelector(".planta-cientifico").textContent =
      planta.nombre_cientifico || "Sin nombre científico";

    const img = clon.querySelector(".card-img-top");
    const icono = clon.querySelector(".icono-planta");

    if (planta.imagen_url && planta.imagen_url.trim() !== "") {
      img.src = planta.imagen_url;
      img.classList.remove("d-none");
      icono.classList.add("d-none");
    } else {
      img.classList.add("d-none");
      icono.classList.remove("d-none");
    }

    clon.querySelector(".invernadero").innerHTML =
      `<i class="bi bi-house-door"></i> ${planta.recinto_id || "Sin ubicación"}`;

    clon.querySelector(".necesita-riego").textContent = "Normal";

    clon.querySelector(".planta-cantidad").textContent = planta.cantidad ?? 0;
    clon.querySelector(".planta-temperatura").textContent = "23º";
    clon.querySelector(".planta-humedad").textContent = "40%";

    const btnEditar = clon.querySelector(".btn-editar");
    const btnEliminar = clon.querySelector(".btn-eliminar");

    btnEditar.addEventListener("click", () => abrirModalEdicion(planta));

    btnEliminar.addEventListener("click", async () => {
      const confirmar = confirm(`¿Quieres eliminar la planta "${planta.nombre}"?`);

      if (!confirmar) return;

      try {
        const response = await fetch(`${API_URL}/plantas/${planta.id}`, {
          method: "DELETE",
        });

        if (!response.ok) throw new Error(`Error ${response.status}`);

        await cargarPlantas();
      } catch (error) {
        console.error("Error al eliminar planta:", error);
      }
    });

    contenedor.appendChild(clon);
  });
}

function obtenerCamposFormulario() {
  const modal = document.querySelector("#plantaNuevaModal");

  return {
    nombre: modal.querySelectorAll("input, textarea, select")[0],
    nombre_cientifico: modal.querySelectorAll("input, textarea, select")[1],
    descripcion: modal.querySelectorAll("input, textarea, select")[2],
    recinto_id: modal.querySelectorAll("input, textarea, select")[3],
    cantidad: modal.querySelectorAll("input, textarea, select")[4],
    fecha_adquisicion: modal.querySelectorAll("input, textarea, select")[5],
    ultimo_riego: modal.querySelectorAll("input, textarea, select")[6],
    imagen_url: modal.querySelectorAll("input, textarea, select")[7],
    notas: modal.querySelectorAll("input, textarea, select")[8],
  };
}

function limpiarFormulario() {
  const campos = obtenerCamposFormulario();

  campos.nombre.value = "";
  campos.nombre_cientifico.value = "";
  campos.descripcion.value = "";
  campos.recinto_id.value = "-- Sin asignar --";
  campos.cantidad.value = 1;
  campos.fecha_adquisicion.value = "";
  campos.ultimo_riego.value = "";
  campos.imagen_url.value = "";
  campos.notas.value = "";

  plantaEditandoId = null;

  document.querySelector(".modal-title span").textContent = "Nueva Planta";
}

function abrirModalEdicion(planta) {
  const campos = obtenerCamposFormulario();

  campos.nombre.value = planta.nombre || "";
  campos.nombre_cientifico.value = planta.nombre_cientifico || "";
  campos.descripcion.value = planta.descripcion || "";
  campos.recinto_id.value = planta.recinto_id || "-- Sin asignar --";
  campos.cantidad.value = planta.cantidad ?? 1;
  campos.fecha_adquisicion.value = planta.fecha_adquisicion || "";
  campos.ultimo_riego.value = planta.ultimo_riego || "";
  campos.imagen_url.value = planta.imagen_url || "";
  campos.notas.value = planta.notas || "";

  plantaEditandoId = planta.id;
  document.querySelector(".modal-title span").textContent = "Editar Planta";

  const modal = new bootstrap.Modal(document.querySelector("#plantaNuevaModal"));
  modal.show();
}

async function guardarPlanta() {
  const campos = obtenerCamposFormulario();

  const planta = {
    nombre: campos.nombre.value.trim(),
    nombre_cientifico: campos.nombre_cientifico.value.trim(),
    descripcion: campos.descripcion.value.trim(),
    recinto_id:
      campos.recinto_id.value === "-- Sin asignar --"
        ? null
        : campos.recinto_id.value,
    cantidad: parseInt(campos.cantidad.value) || 1,
    fecha_adquisicion: campos.fecha_adquisicion.value,
    ultimo_riego: campos.ultimo_riego.value,
    imagen_url: campos.imagen_url.value.trim(),
    notas: campos.notas.value.trim(),
  };

  if (!planta.nombre) {
    alert("El nombre de la planta es obligatorio");
    return;
  }

  try {
    let response;

    if (plantaEditandoId) {
      response = await fetch(`${API_URL}/plantas/${plantaEditandoId}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(planta),
      });
    } else {
      response = await fetch(`${API_URL}/plantas`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(planta),
      });
    }

    if (!response.ok) {
      const errorData = await response.json();
      alert(errorData.detail || "Ha ocurrido un error");
      return;
    }

    const modalElement = document.querySelector("#plantaNuevaModal");
    const modalInstance = bootstrap.Modal.getInstance(modalElement);
    if (modalInstance) {
      modalInstance.hide();
    }

    limpiarFormulario();
    await cargarPlantas();
  } catch (error) {
    console.error("Error al guardar planta:", error);
  }
}

document.addEventListener("hidden.bs.modal", function (event) {
  if (event.target.id === "plantaNuevaModal") {
    limpiarFormulario();
  }
});