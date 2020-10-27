from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
class IndexView(TemplateView):
    template_name = "index.html"
async def websocket_view(socket):
    await socket.accept()
    await socket.send_text('hello')
    await socket.close()
