$(document).ready(function () {
  // Mostrar mensaje al hacer clic en el botón
  $("#show-message").click(function () {
    $("#message").toggleClass("hidden");
  });

  // Mostrar/Ocultar imagen al hacer clic en el botón
  $("#toggle-image").click(function () {
    $("#logo").toggle();
  });

  // Evento de envío de formulario
  $("#my-form").submit(function (event) {
    event.preventDefault();
    const name = $("#name").val();
    const email = $("#email").val();
    $("#form-result")
      .html(`<p>Nombre: ${name}</p><p>Email: ${email}</p>`)
      .removeClass("hidden");
  });

  // Eventos de teclado
  $("#name").keydown(function () {
    console.log("Tecla presionada en el campo de nombre");
  });

  $("#email").keyup(function () {
    console.log("Tecla soltada en el campo de email");
  });

  // Evento de enfoque
  $("#name")
    .focus(function () {
      $(this).css("background-color", "#e0e0e0");
    })
    .blur(function () {
      $(this).css("background-color", "#fff");
    });

  // Animación
  $("#toggle-image").click(function () {
    $("#logo").fadeToggle();
  });

  // Cambio de contenido
  $("#show-message").click(function () {
    $(this).text(
      $(this).text() === "Mostrar Mensaje"
        ? "Ocultar Mensaje"
        : "Mostrar Mensaje"
    );
  });

  // Eventos del mouse
  $("#show-message").hover(
    function () {
      $(this).css("background-color", "#28a745");
    },
    function () {
      $(this).css("background-color", "#007bff");
    }
  );

  // Efecto de deslizamiento
  $("#animate-div").click(function () {
    $("#anim-div").slideToggle();
  });

  // Evento de doble clic
  $("#anim-div").dblclick(function () {
    alert("Div doble clicado");
  });

  // Clonación de elementos
  $("#clone-button").click(function () {
    $(".clonable").clone().appendTo("#button-container");
  });

  // Append text
  $("#append-text").click(function () {
    $("#text-container").append("<p>Nuevo texto agregado</p>");
  });

  // Evento de scroll
  $(window).scroll(function () {
    console.log("Scroll detectado");
  });

  // Cambio de atributos
  $("#toggle-image").click(function () {
    let src =
      $("#logo").attr("src") === "assets/logo.png"
        ? "assets/logo-alt.png"
        : "assets/logo.png";
    $("#logo").attr("src", src);
  });

  // Obtener valores de atributos
  $("#show-message").click(function () {
    console.log("Atributo src del logo:", $("#logo").attr("src"));
  });

  // Efecto de fadeIn y fadeOut
  $("#toggle-image").click(function () {
    $("#logo").fadeToggle();
  });

  // Efecto de slideUp y slideDown
  $("#animate-div").click(function () {
    $("#anim-div").slideToggle();
  });

  // Evento on
  $("#append-text").on("click", function () {
    console.log("Evento on click");
  });

  // Evento off
  $("#append-text").off("click");
});
