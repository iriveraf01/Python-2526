/// <reference types="jquery" />
$(function () {
  $("#contenido").load("dashboard.html");
  $(document).on(
    "click",
    "#dashboard, #recintos, #inventario, #reportes, #configuracion",
    function () {
      $(".nav .nav-link").removeClass("active");
      $(this).addClass("active");
      $("#contenido").load(`${this.id}.html`);
    }
  );
});
