import os
from pathlib import Path
from django import db


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '&s8g9dsadsasadsadfcdsa^%#*m&^!htrm(1j2!01iht#@btgd654%re7rg7'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [

    # My apps
    'social',
    'accounts',

    # Default apps

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # Third Party Libraries
    'crispy_forms',
    'widget_tweaks',
    "debug_toolbar",

    # 'pagedown',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'Vitbook.urls'
USER_AVATAR_URL = 'default_profile.png'
WSGI_APPLICATION = 'Vitbook.wsgi.application'
DEFAULT_AUTO_FIELD='django.db.models.AutoField' 
LOGIN_REDIRECT_URL = "/"
CSRF_TRUSTED_ORIGINS = ['https://vitbook.azurewebsites.net','https://*.127.0.0.1']


# django debug toolbar

INTERNAL_IPS = ["127.0.0.1"] 

if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]



# Database


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'BigProject'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vitbook-postgres-db',
        'USER': 'vitbook_admin_db@vitbook-postgres-db',
        'PASSWORD': os.getenv("VITBOOK_DB_PASS"),
        'HOST': 'vitbook-postgres-db.postgres.database.azure.com',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'}
    }
}

# DJANGO DEFAULTS - Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# sample static file config
STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"