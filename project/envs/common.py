from os.path import abspath, join, dirname
from sys import path
from envs.keys_and_passwords import *

PROJECT_ROOT = abspath(join(dirname(__file__), "../"))
APPS_DIR = abspath(join(dirname(__file__), "../", "apps"))
path.insert(0, PROJECT_ROOT)
path.insert(0, APPS_DIR)


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Steven Skoczen', 'skoczen@gmail.com'),
)

MANAGERS = ADMINS
EMAIL_SUBJECT_PREFIX = "[Schizophrenia Survey] "
SERVER_EMAIL = 'skoczen@gmail.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'schizophrenia',
        'USER': '',
        'PASSWORD': DB_PASSWORD,
        'HOST': '',
        'PORT': '',
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

ALLOWED_HOSTS = ["qi-schizophrenia-staging.herokuapp.com", "qi-schizophrenia-live.herokuapp.com"]

TIME_ZONE = 'America/Vancouver'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False
USE_L10N = True

MEDIA_ROOT = join(PROJECT_ROOT, "media_root")
MEDIA_URL = '/media/'

STATIC_ROOT = join(PROJECT_ROOT, "collected_static")
STATIC_URL = '/static/'

STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = '^7!$isr6jd!o+mgl1qy@+8197dm53uhp2i*vp8k4p#*g#8mg1n'

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
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    join(abspath(PROJECT_ROOT),"templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    "analytical",
    "annoying",
    "compressor",
    "django_extensions",

    "gunicorn",
    "south",

    "main_site",
    "survey",
    "utils",


    # Must come after south
    "django_nose",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
)


STATICFILES_EXCLUDED_APPS = []
COMPRESS_ROOT = STATIC_ROOT

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
GOOGLE_ANALYTICS_PROPERTY_ID = ""
GAUGES_SITE_ID = ""


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
SOUTH_TESTS_MIGRATE = False
