$(document).ready(function () {
  // Activate tooltip
  $('[data-toggle="tooltip"]').tooltip();

  // Event click on "Enviar por correo"
  $("#enviarCorreo").click(function () {
    alert("El correo fue enviado correctamente...");
  });

  // Double click en INGREDIENTES y PREPARACIÓN
  $("h2").dblclick(function () {
    $(this).css("color", "red");
  });

  // Toggle card content
  $(".card-title").click(function () {
    $(this).next(".card-text").toggle();
  });
});
