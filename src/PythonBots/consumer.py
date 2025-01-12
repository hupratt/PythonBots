import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.db import database_sync_to_async



class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected",event)
        await self.send({
            "type":"websocket.accept"
        })
    async def websocket_receive(self, event):
        print("receive",event)
    async def websocket_disconnect(self, event):
        print("disconnected",event)

