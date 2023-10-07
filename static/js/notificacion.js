document.addEventListener('DOMContentLoaded', function() {
    var messagesContainer = document.querySelector('.cont-messages');
    if (messagesContainer) {
      // Muestra la notificación
      messagesContainer.style.display = 'block';

      // Recorre los mensajes y agrega clases de estilo según el tipo de mensaje
      var messages = messagesContainer.querySelectorAll('li');
      messages.forEach(function(message) {
        if (message.classList.contains('true')) {
          message.classList.add('success');
        } else if (message.classList.contains('false')) {
          message.classList.add('error');
        }
      });

      // Oculta la notificación después de 5 segundos (5000 ms)
      setTimeout(function() {
        messagesContainer.style.display = 'none';
      }, 4000);
    }
});