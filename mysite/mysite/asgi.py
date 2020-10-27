"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os
import django

from django.core.asgi import get_asgi_application
# from django.core.asgi import get_asgi_application
from websocket.middleware import websockets

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")


django.setup()
# application = get_asgi_application()
application = get_asgi_application()
application = websockets(application)
