from django.urls import re_path # Para que eu possa utilizar expressão regular
from . import consumers, AsyncConsumers # Eu que inventei o nome AsyncConsumers para diferenciar do verdadeiro consumers

websocket_url_patterns = [
    re_path(r'ws/app/(?P<nome>\w+)/$', AsyncConsumers.TesteConsumer.as_asgi()) # URL do Channels que recebe um parâmetro nome (regex)
]