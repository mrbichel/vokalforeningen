import os
import sys
import site

site.addsitedir('/home/vokal/.virtualenvs/vokal/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()