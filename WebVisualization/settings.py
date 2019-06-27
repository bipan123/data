"""
Django settings for WebVisualization project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import redis as redis
from flask import Flask
from flask_sockets import Sockets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x-v$qxhbfy+jse*f)mx7(r_@_h#3rwo-o36t5j#pnhh25%8h*2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/login/'

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webViz.apps.WebvizConfig',
    'rest_framework',
    'django_filters',
    'rest_framework_filters',
    'channels',

]

# REDIS_URL = os.environ['REDIS_URL']

REDIS_URL = "redis://h:pb7db417bc4315578831fd6ee5f9728ef080116d100f144e403535878eb20a914@ec2-35-175-40-87.compute-1.amazonaws.com:29199"

# REDIS_URL = "redis://127.0.0.1:6379"


REDIS_CHAN = 'chat'

CHANNEL_LAYERS = {
    'default': {

        'CONFIG': {
            'hosts': [REDIS_URL, ],
        },
        'BACKEND': 'channels_redis.core.RedisChannelLayer',

    }
}

ASGI_APPLICATION = 'WebVisualization.routing.application'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'WebVisualization.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'WebVisualization.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'postgres-server': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rm_data_sushant',
        'USER': 'rmserver_docker_sushant',
        'PASSWORD': 'rmserver_docker_sushant',
        'HOST': '210.127.211.112',
        'PORT': '5432',
    },
    'serveo-server': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rm_data_sushant',
        'USER': 'rm_data_sushant',
        'PASSWORD': 'rm_data_sushant',
        'HOST': 'serveo.net',
        'PORT': '5433',
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())

app = Flask(__name__)

sockets = Sockets(app)
redis = redis.from_url(REDIS_URL)
