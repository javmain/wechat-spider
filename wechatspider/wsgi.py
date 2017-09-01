"""
WSGI config for wechatspider project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
print sys.path
sys.path.append('/home/provisional/.pyenv/versions/2.7.13/lib/python2.7/site-packages')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wechatspider.settings")

application = get_wsgi_application()
