# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class IntermediateResultConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("intermediate_results", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("intermediate_results", self.channel_name)

    async def send_intermediate_result(self, event):
        print("consumer send noti")
        result = event['result']
        await self.send(text_data=json.dumps({
            'result': result
        }))
