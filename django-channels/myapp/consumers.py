# Importa o módulo 'json' para manipulação de dados em formato JSON
import json  
# Importa a classe 'WebsocketConsumer' da biblioteca Channels para criar consumidores WebSocket
from channels.generic.websocket import WebsocketConsumer  
from asgiref.sync import async_to_sync

# Define uma classe 'TesteConsumer' que herda de 'WebsocketConsumer'
class TesteConsumer(WebsocketConsumer):  
    
    # Método chamado quando uma conexão WebSocket é estabelecida
    def connect(self):
        self.room_group_name = 'todos'
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        # Aceita a conexão WebSocket. Isso permite que a comunicação WebSocket continue
        self.accept()  

    # Método chamado quando a conexão WebSocket é fechada
    def disconnect(self, close_code): 
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Método chamado quando uma mensagem é recebida através da conexão WebSocket
    def receive(self, text_data):  
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))