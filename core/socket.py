import socketio 
from django.conf import settings

#Criando o server do SOCKETIO
socket = socketio.Server(
    cors_allowed_origins=settings.CORS_ALLOWED_ORIGINS
)