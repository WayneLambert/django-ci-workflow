import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ['DJANGO_SETTINGS_MODULE'])

application = get_asgi_application()
