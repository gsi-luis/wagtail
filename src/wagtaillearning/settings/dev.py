from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'd@8681qm+38ktba==zj^1ql=c7+0f5uh==u^5(4(&akbx%1x^c'

# SECURITY WARNING: define the correct hosts in production!
#ALLOWED_HOSTS = ['*'] 

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
