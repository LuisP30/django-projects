# Importa o módulo 'json' para manipulação de dados em formato JSON
import json  
# Importa a classe 'WebsocketConsumer' da biblioteca Channels para criar consumidores WebSocket
from channels.generic.websocket import WebsocketConsumer  

# Define uma classe 'TesteConsumer' que herda de 'WebsocketConsumer'
class TesteConsumer(WebsocketConsumer):  
    
    # Método chamado quando uma conexão WebSocket é estabelecida
    def connect(self):
        # Aceita a conexão WebSocket. Isso permite que a comunicação WebSocket continue
        self.accept()  

    # Método chamado quando a conexão WebSocket é fechada
    def disconnect(self, code): 
        
        # O método 'disconnect' não faz nada neste exemplo. O 'code' é o código de desconexão fornecido pelo WebSocket
        pass  

    # Método chamado quando uma mensagem é recebida através da conexão WebSocket
    def receive(self, text_data):  
        # Converte os dados de texto recebidos (em JSON) para um dicionário Python
        text_data_json = json.loads(text_data)  
        
        # Extrai a mensagem do dicionário usando a chave 'message'
        message = text_data_json['message']  

        # Envia uma resposta de volta para o cliente WebSocket
        self.send(text_data=json.dumps({  
            # Inclui a mensagem recebida na resposta, formatada em JSON
            'message': message  
        }))
