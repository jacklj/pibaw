from .base import *


DEBUG = False
ALLOWED_HOSTS = ['jackvlj.pythonanywhere.com', 'www.picturesinblackandwhite.com', 'picturesinblackandwhite.com', 'www.picturesinblackandwhite.co.uk', 'picturesinblackandwhite.co.uk']

SECRET_KEY = 'n(1w5+i^7nn&bu_5rz^u=1&+xn^c3jml(@ff()r+q8qyh%d1@d'


try:
    from .local import *
except ImportError:
    pass
