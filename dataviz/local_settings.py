"""
Local-specific settings. 
Maintain high-protection prod settings while 
enabling rapid development on your local.
"""
# from .base_settings import *

DEBUG = True

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False