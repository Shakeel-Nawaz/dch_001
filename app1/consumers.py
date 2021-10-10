from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'priv'
        self.room_group_name = 'privgrp'
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status':'connected'}),close=False)
        # return super().connect()
    def receive(self, text_data=None, bytes_data=None):
        self.text_data = text_data
        self.send(text_data=json.dumps(self.text_data))
        # return super().receive(text_data=text_data, bytes_data=bytes_data)
    def disconnect(self, code):
        print(code)
        # return super().disconnect(code)