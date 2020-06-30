import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '&s8g9^%#jl356^%#*m&^!htrm(1j2!01iht#@btgd654%re7rg7'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [

    # My apps
    'social',
    'registration',

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

    # 'pagedown',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#
# MIDDLEWARE = [
#
#     # DJANGO DEFAULTS
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#
#     # CUSTOM CATCHING TECHNIQUE  -  CATCHING MIDDLEWARE
#     'django.middleware.cache.UpdateCacheMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     # 'django.middleware.cache.FetchFromCacheMiddleware',
#
#     # DJANGO DEFAULTS
#     # 'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#
# ]

ROOT_URLCONF = 'Vitbook.urls'

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

WSGI_APPLICATION = 'Vitbook.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'BigProject'),
    }
}

# IN CASE DATABASE NEED TO BE SWITCHED FROM SQLITE TO VITBOOK

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'USER' : 'postgres',
#         'NAME' : 'BigProject',
#         'HOST' : 'localhost',
#         'PASSWORD' : 'password'
#     }
# }

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

# Static files (CSS, JavaScript, Images)

LOGIN_REDIRECT_URL = "/"
STATIC_ROOT = os.path.join(BASE_DIR + 'staticfiles')

STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR + '/static/images')


ACCOUNT_ACTIVATION_DAYS = 3

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'vitbook.smtp.team@gmail.com'
EMAIL_HOST_PASSWORD = 'ErqmsQF8pF5KEFg'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'




# CHACHE SETTING (INTEGRATION WITH Memcached Framework)

# CACHES = {
#     'default':{
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1;11211',
#     }
# }

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'vitbook_cache',
#     }
# }
