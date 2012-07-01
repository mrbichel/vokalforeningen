# coding=utf-8
import os.path
import sys
import platform

PRODUCTION_HOSTNAME = "tango"

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

ROOT_URLCONF = 'vokalforeningen.urls'

sys.path.append(BASE_PATH + '/apps')

ADMINS = (
    ('Johan Bichel Lindegaard', 'sysadmin@tango.johan.cc'),
)
MANAGERS = ADMINS + (
    ('Malene Bichel', 'malenebi@gmail.com'),
    ('Dorte Hyldstrup', 'dortehyldstrup@dortehyldstrup.dk')
)

AUTHENTICATION_BACKENDS = ('backends.EmailBackend',
    "django.contrib.auth.backends.ModelBackend",)

DEVELOPMENT_MODE = (platform.node() != PRODUCTION_HOSTNAME)
if DEVELOPMENT_MODE:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEBUG = True
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
else:
    DEBUG = False
    MEDIA_URL = 'http://media.vokalforening.dk/'
    STATIC_URL = 'http://static.vokalforening.dk/'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

# Static files
MEDIA_ROOT = BASE_PATH + '/../media'
STATICFILES_DIRS = (
    BASE_PATH + '/../static',
)

TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'da'
SITE_ID = 1
USE_I18N = True
USE_L10N = False

LOCALE_PATHS = (
    BASE_PATH + '/locale',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_DIRS = (
    BASE_PATH + '/templates/'
)

DATE_INPUT_FORMATS = ('%m/%d/%Y', '%Y-%m-%d', '%m/%d/%y', '%b %d %Y',
'%b %d, %Y', '%d %b %Y', '%d %b, %Y', '%B %d %Y',
'%B %d, %Y', '%d %B %Y', '%d %B, %Y')

INSTALLED_APPS = (
    # Apps
    'corkboard',
    'meetings',
    'profiles',

    # Third-party
    'south',
    'sorl.thumbnail',
    'notification',

    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.sitemaps',
    'django.contrib.comments',
    'django.contrib.flatpages',
)

AUTH_PROFILE_MODULE = 'profiles.Profile'

LOGIN_REDIRECT_URL = "/i"

DATE_FORMAT = "j N Y"
TIME_FORMAT = "H:i"
DATETIME_FORMAT = "j N Y H:i"
PAGINATE_BY = 12

DEFAULT_FROM_EMAIL = "server@vokalforening.dk"
SERVER_EMAIL = "server@vokalforening.dk"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
	'sorl.thumbnail': {
            'handlers':  ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


try:
    execfile(BASE_PATH + '/settings_local.py')
except IOError:
    sys.stderr.write("\nYou need to copy settings_local.example to settings_local.py and customize it.\n")
    sys.exit(1)
