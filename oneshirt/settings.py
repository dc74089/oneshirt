"""
Django settings for oneshirt project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

is_prod = os.getenv('ONESHIRT_PROD')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if is_prod:
    SECRET_KEY = os.getenv("ONESHIRT_SECRET")
else:
    SECRET_KEY = '@0r_6q=(vqxsc^=@0+e%athr60zb9#^#wa3knh0*5vax%v()zx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not is_prod

ALLOWED_HOSTS = ['1shirt.trade', 'www.1shirt.trade']

if not is_prod:
    ALLOWED_HOSTS.append('dev.1shirt.trade')
    ALLOWED_HOSTS.append('10.19.2.2')
    ALLOWED_HOSTS.append('127.0.0.1')
    ALLOWED_HOSTS.append('localhost')


# Application definition

INSTALLED_APPS = [
    'trade',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'oneshirt.urls'

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

WSGI_APPLICATION = 'oneshirt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oneshirt',
        'USER': 'oneshirt',
        'PASSWORD': os.getenv("ONESHIRT_DB_PASS"),
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {'init_command': 'SET storage_engine=MyISAM', },
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


if is_prod:
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

if is_prod:
    ADMINS = [("Dominic", os.getenv("ADMIN_EMAIL"))]

if is_prod:
    EMAIL_HOST_USER = "noreply@mail.oneshirt.trade"
    EMAIL_HOST_PASSWORD = os.getenv("ONESHIRT_SMTP_PASS")
else:
    EMAIL_HOST_USER = "mail-dev@mail.oneshirt.trade"
    EMAIL_HOST_PASSWORD = os.getenv("ONESHIRT_SMTP_DEV_PASS")


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/oneshirt/static/'
if is_prod:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = '/home/pedia/media/'
else:
    ENV_PATH = os.path.abspath(os.path.dirname(__file__))
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(ENV_PATH, 'media/')
