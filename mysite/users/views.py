from django.urls import resolve
from websocket.connection import WebSocket
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

async def websocket_view(socket: WebSocket):
    await socket.accept()
    while True:
        message = await socket.receive_text()
        await socket.send_text(message)
