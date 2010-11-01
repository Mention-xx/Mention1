#!/usr/bin/env python
import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'timesheet.settings'

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

