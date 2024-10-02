# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.group_name = self.scope['url_route']['kwargs']['group_name']

		# Присоединяемся к группе чата
		await self.channel_layer.group_add(self.group_name, self.channel_name)

		await self.accept()

	async def disconnect(self, close_code):
		# Отключаемся от группы чата
		await self.channel_layer.group_discard(self.group_name, self.channel_name)

	async def receive(self, text_data):
		data = json.loads(text_data)

		message = data['message']

		# Отправляем сообщение в группу чата
		await self.channel_layer.group_send(
			self.group_name,
			{
				'type': 'chat_message',
				'message': message,
				'sender': self.scope['user'].username,
			}
		)

	async def chat_message(self, event):
		message = event['message']
		sender = event['sender']

		# Отправляем сообщение пользователю
		await self.send(text_data=json.dumps({
			'message': message,
			'sender': sender,
		}))