#!/usr/bin/python
#coding:utf-8
"""
WSGI config for spidermanage project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from nmaptoolbackground.control import taskcontrol
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spidermanage.settings")

application = get_wsgi_application()
taskcontrol.scheduleinit()