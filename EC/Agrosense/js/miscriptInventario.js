export function inicializarInventario() {
  cargarPlantas()
}
const API_URL = "http://127.0.0.1:8001";

async function cargarPlantas() {
    const response = await fetch(`${API_URL}/plantas`);
    if (!response.ok) throw new Error(`Error ${response.status}`);

    const plantas = await response.json();
    console.log(plantas);

    const temp = document.querySelector("#templateTarjetaPlanta");
    const contenedor = document.querySelector(".contenedorTarjetas");

    contenedor.innerHTML = "";

    plantas.forEach((planta) => {
      
      const clon = temp.content.cloneNode(true);

      clon.querySelector(".planta-nombre").textContent =
        planta.nombre || "Sin nombre";

      clon.querySelector(".planta-cientifico").textContent =
        planta.nombre_cientifico || "Sin nombre científico";

      clon.querySelector(".card-img-top").src = planta.imagen_url || '<i class="bi bi-flower1"></i>'

      clon.querySelector(".invernadero").innerHTML =
        `<i class="bi bi-house-door"></i> ${planta.ubicacion || "Sin ubicación"}`;

      clon.querySelector(".necesita-riego").textContent =
        planta.necesita_riego ? "Necesita riego" : "No necesita riego";

      clon.querySelector(".planta-cantidad").textContent =
        planta.cantidad ?? 0;

      clon.querySelector(".planta-temperatura").textContent =
        `${planta.temperatura ?? "--"}º`;

      clon.querySelector(".planta-humedad").textContent =
        `${planta.humedad ?? "--"}%`;

      contenedor.appendChild(clon);
    });
}