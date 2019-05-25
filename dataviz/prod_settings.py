"""
Production-Specific settings. 
Maintain high-protection prod settings while 
enabling rapid development on your local.
"""
from .base_settings import *

DEBUG = False

SECURE_HSTS_SECONDS = 518400
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'