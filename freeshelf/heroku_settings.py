from freeshelf.settings import *

import django_heroku

DEBUG = False

django_heroku.settings(locals())