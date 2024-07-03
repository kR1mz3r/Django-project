import hashlib
import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_group_name = 'group_chat_gfg'
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
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        recipient = text_data_json['recipient']
        conversation_id = await self.save_message(message, sender, recipient)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender,
                'recipient': recipient,
                'conversation_id': conversation_id
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        recipient = event['recipient']
        conversation_id = event['conversation_id']
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'recipient': recipient,
            'conversation_id': conversation_id
        }))

    @database_sync_to_async
    def save_message(self, message, sender_username, recipient_username):
        sender = User.objects.get(username=sender_username)
        recipient = User.objects.get(username=recipient_username)
        user_ids = [str(sender.id), str(recipient.id)]
        sorted_user_ids = '-'.join(sorted(user_ids))
        conversation_id = hashlib.sha256(sorted_user_ids.encode()).hexdigest()
        Message.objects.create(
            sender=sender,
            recipient=recipient,
            content=message,
            conversation_id=conversation_id
        )
        return conversation_id
