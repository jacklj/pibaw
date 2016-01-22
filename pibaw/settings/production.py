from .base import *


DEBUG = False
ALLOWED_HOSTS = ['jackvlj.pythonanywhere.com']

SECRET_KEY = 'n(1w5+i^7nn&bu_5rz^u=1&+xn^c3jml(@ff()r+q8qyh%d1@d'


try:
    from .local import *
except ImportError:
    pass
