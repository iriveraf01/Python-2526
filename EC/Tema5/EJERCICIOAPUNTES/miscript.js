const API_URL = "http://127.0.0.1:8001";
const btnConsultar = document.querySelector("#btnConsultar");
const inputCiudad = document.querySelector("#city");
const weatherTemplate = document.querySelector("#weatherTemplate");
const divResultado = document.querySelector("#resultado");
const errorTemplate = document.querySelector("#errorTemplate");

consultarTiempo();
btnConsultar.addEventListener("click", consultarTiempo);

async function consultarTiempo() {
  const ciudad = inputCiudad.value.trim();
  if (ciudad === "") {
    alert("Por favor, ingresa el nombre de una ciudad.");
    return;
  }
  const params = new URLSearchParams({ ciudad: ciudad });
  const response = await fetch(`${API_URL}/api/weather?${params}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (!response.ok) {
    throw new Error("Error al delvolver datos de la previsión");
  }
  const data = await response.json();
  mostrarResultado(data);
}

function mostrarResultado(data) {
  const clon = weatherTemplate.content.cloneNode(true);
  clon.querySelector(".city-name").textContent = data.ciudad;
  clon.querySelector(".temperature").textContent = data.temperatura + "°C";
  clon.querySelector(".feels-like").textContent = data.sensacion + "°C";
  clon.querySelector(".humidity").textContent = data.humedad + "%";
  clon.querySelector(".description").textContent = data.descripcion;
  clon.querySelector(".weather-icon").src =
    `https://openweathermap.org/img/wn/${data.icono}@2x.png`;
  clon.querySelector(".wind").textContent = data.viento + " m/s";

  divResultado.innerHTML = "";
  divResultado.appendChild(clon);
}

function mostrarError(mensaje) {
  const clon = errorTemplate.content.cloneNode(true);
  clon.querySelector(".error-message").textContent = mensaje;
  divResultado.innerHTML = "";
  divResultado.appendChild(clon);
}
