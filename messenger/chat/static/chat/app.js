const messagesContainer = document.getElementById('messages');
const messageInput = document.getElementById('messageInput');
const sendMessageButton = document.getElementById('sendMessage');

let socket;

function connectToChat(groupName) {
   socket = new WebSocket(`ws://${window.location.host}/ws/chat/${groupName}/`);

   socket.onmessage = function(event) {
       const data = JSON.parse(event.data);

       const messageDiv = document.createElement('div');
       messageDiv.innerText = `${data.sender}: ${data.message}`;

       messagesContainer.appendChild(messageDiv);
   };

   socket.onclose = function(event) {
       console.error('WebSocket closed unexpectedly');
   };
}

// Отправка сообщения в текущий групповой чат.
sendMessageButton.onclick = async () => {
   const messageContent = messageInput.value;

   if (messageContent) {
       socket.send(JSON.stringify({
           'message': messageContent,
       }));

       messageInput.value = ''; // Очистка поля ввода сообщения.
   }
};

// Инициализация приложения.
connectToChat('default'); // Подключение к чату по умолчанию или выбранному чату.