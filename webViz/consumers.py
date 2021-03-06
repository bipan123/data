import json
import binascii
from ast import literal_eval as make_tuple
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.views.decorators.clickjacking import xframe_options_exempt

from webViz.reciever import decrypteddata
@xframe_options_exempt
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "BoothMasterSocket"
        self.room_group_name = 'booth_updates'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        self.accept()

        '''async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': "refreshall",
                'boothname': "boothmaster",

            }
        ) '''

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data, ):
        text_data_json = json.loads(text_data)
        message1 = text_data_json['message']
        decdata=binascii.unhexlify(message1)
        decrypt_message = decrypteddata(decdata)
        data_tuple=make_tuple(decrypt_message.decode())
        message = data_tuple
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message' : message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        temp = message[0]
        hum = message[1]
        lat = message[2]/100
        lon = message[3]/100

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'temp': temp,
            'hum': hum,
            'lat': lat,
            'lon': lon,
            'ifsuccess': 'success',
        }))
