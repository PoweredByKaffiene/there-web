import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class LocationConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.accept()

    def receive(self, text_data):
        username = self.scope["user"]
        if(username.is_authenticated()):
            text_json = json.loads(text_data)
            print(text_json)
            self.send(text_data=json.dumps({'message': text_json}))
        self.send(text_data="")
