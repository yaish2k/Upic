"""
WSGI config for Upic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import threading

def printInit():
    threading.Timer(5.0,printInit).start()
    print "hello world"
printInit()


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Upic.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
