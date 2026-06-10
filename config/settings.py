import os
import environ
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment schema router
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(str(BASE_DIR / '.env'))
# Read the hidden .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Cryptographic Keys & Rules
SECRET_KEY = env('SECRET_KEY', default='django-insecure-j+m8@6%vjx8^uxbhi0mdz%q6-^e@%vi!j3&jtnf%!v@$u9)nsv')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['10.128.233.97', '127.0.0.1', 'localhost'])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ludotheque',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database Dynamic Routing (Points directly to MariaDB via .env variables)
if os.getenv('DEBUG') == 'True':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # Ici, garde ton ancienne configuration MySQL pour la production
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'assignment_ludo',
            'USER': 'ludo_admin',
            'PASSWORD': 'LudoSAE2026',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Assets Architecture
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = ['http://10.128.207.224', 'http://10.128.208.51']
