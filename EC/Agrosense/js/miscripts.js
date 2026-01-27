/// <reference types="jquery" />
$(function () {
  const contenido = document.querySelector("#contenido");
  loadHTML("dashboard.html", contenido);

  document.addEventListener("click", function (evento) {
    const elementosValidos = [
      "dashboard",
      "recintos",
      "inventario",
      "reportes",
      "configuracion",
    ];

    if (elementosValidos.includes(evento.target.id)) {
      document.querySelectorAll(".nav .nav-link").forEach((link) => {
        link.classList.remove("active");
      });
      evento.target.classList.add("active");
      loadHTML(`${evento.target.id}.html`, contenido);
    }
  });

  async function loadHTML(url, objetivo) {
    const respuesta = await fetch(url);
    objetivo.innerHTML = await respuesta.text();
  }

  // $("#contenido").load("dashboard.html");
  // $(document).on(
  //   "click",
  //   "#dashboard, #recintos, #inventario, #reportes, #configuracion",
  //   function () {
  //     $(".nav .nav-link").removeClass("active");
  //     $(this).addClass("active");
  //     $("#contenido").load(`${this.id}.html`);
  //   }
  // );
});
