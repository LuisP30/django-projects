# Importa o módulo 'json' para manipulação de dados em formato JSON
import json  
# Importa a classe 'WebsocketConsumer' da biblioteca Channels para criar consumidores WebSocket
from channels.generic.websocket import AsyncWebsocketConsumer  

# Define uma classe 'TesteConsumer' que herda de 'WebsocketConsumer'
class TesteConsumer(AsyncWebsocketConsumer):  
    
    # Método chamado quando uma conexão WebSocket é estabelecida
    async def connect(self):
        # print(self.scope) # Scope é como se fosse a request 
        self.room_group_name = self.scope['url_route']['kwargs']['nome'] # Atribuindo um grupo ao usuário que conectou
        print(self.room_group_name)
        await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
        
        # Aceita a conexão WebSocket. Isso permite que a comunicação WebSocket continue
        await self.accept()  

    # Método chamado quando a conexão WebSocket é fechada
    async def disconnect(self, close_code): 
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Método chamado quando uma mensagem é recebida através da conexão WebSocket
    async def receive(self, text_data):  
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))