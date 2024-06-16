# chatapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = f'user_{self.user.username}'
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        to_user = data['to']

        await self.channel_layer.group_send(
            f'chat_user_{to_user}',
            {
                'type': 'chat_message',
                'message': message,
                'from': self.user.username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        from_user = event['from']

        await self.send(text_data=json.dumps({
            'message': message,
            'from': from_user,
        }))
