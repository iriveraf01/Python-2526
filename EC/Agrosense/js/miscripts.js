/// <reference types="jquery" />
$(function () {
  //Todo lo que metas aquí se ejecutará cuando se haya cargado TODO el HTML
  $(document).on("click", "#recintos", function (e) {
    e.preventDefault();

    $(".nav-link").removeClass("active");
    $(this).addClass("active");

    //Se asocia click al ID recinto
    $("#contenido").load("recintos.html"); //En ID contenido se mete elcontenido de recintos.html
  });

  $(document).on("click", "#dashboard", function (e) {
    e.preventDefault();

    $(".nav-link").removeClass("active");
    $(this).addClass("active");

    $("#contenido").load("dashboard.html");
  });
});
