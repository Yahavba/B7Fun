# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

"""
Django settings for B7FunDjango project.

Generated by 'django-admin startproject' using Django 2.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import sys
import os
from django.contrib.admin import AdminSite

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h&fr0w!&udq9qu$n+w7-(d&0=it7x^0(22t%_#6v!ix$jk3d9*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leaflet',
    'accounts',
    'feed',
    'Profile',
    'postsFeed',
    'reviews',
    'chat',
    'channels',
    'reports',
    'adminStats',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'B7FunDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates'))],
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

WSGI_APPLICATION = 'B7FunDjango.wsgi.application'

ASGI_APPLICATION = 'B7FunDjango.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)]
        },
    },
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'B7FunDb',
            'CLIENT': {
                'host': 'mongodb+srv://B7Fun:B7FunDb@b7fun-2ldf3.' +
                        'mongodb.net/test?retryWrites=true&w=majority',
                'username': 'B7Fun',
                'password': 'B7FunDb',
                'authMechanism': 'SCRAM-SHA-1'
            }
        }
    }

AUTH_USER_MODEL = 'accounts.User'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Israel'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# mail service
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'b7funservice@gmail.com'
EMAIL_HOST_PASSWORD = 'ttxankkfptlfblto'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# logout when browser close
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


LOGOUT_REDIRECT_URL = "/login"
LOGIN_URL = "/login"

# testing
TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
TEST_OUTPUT_DIR = './test_reports'
TEST_OUTPUT_FILE_NAME = 'unittest.xml'
TEST_OUTPUT_VERBOSE = 0


# maps
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (31.2530, 34.7915),
    'DEFAULT_ZOOM': 12,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'RESET_VIEW': False
}


# add logging to template

if 'test' not in sys.argv:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
    }

# admin site settings
AdminSite.site_header = 'B7Fun administration'
AdminSite.site_title = 'B7Fun administration'
AdminSite.site_url = '/feed'
AdminSite.index_title = 'B7Fun administration'