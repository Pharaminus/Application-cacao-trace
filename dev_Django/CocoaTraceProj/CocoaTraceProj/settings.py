"""
Django settings for CocoaTraceProj project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i@czdfu4+u8=(8@=%zlo@v-96tfu^k&i_p#s1d!-u4b3+%wt%p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = [
#     "127.0.0.1",
#     "localhost",
#     "3b98-129-0-226-169.ngrok-free.app",  # Ajoutez l'URL ngrok ici
# ]


# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
#     'https://356e-129-0-205-128.ngrok-free.app/',
#     'https://3b98-129-0-226-169.ngrok-free.app/',
#     # Adresse de votre frontend React
# ]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'corsheaders',
    'rest_framework',
    'cocoaApp',
    'rest_framework.authtoken',
    
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]
CORS_ALLOWED_ORIGINS = [
    "http://192.168.1.194:3000",  # React frontend
    "http://localhost:3000",  # React frontend
]

CSRF_TRUSTED_ORIGINS = [
    "http://192.168.1.194:3000",  # Ajoute localhost comme origine fiable
#     "http://localhost:3000",  # Ajoute localhost comme origine fiable
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True


CORS_ALLOWED_METHODS = [
    'GET',
    'POST',
    'PUT',
    'DELETE',
    'OPTIONS',
]

CSRF_COOKIE_HTTPONLY = False  # Doit être False pour que React puisse le lire
CSRF_COOKIE_SAMESITE = "Lax"  # Permet d'envoyer le cookie avec des requêtes cross-origin
SESSION_COOKIE_SAMESITE = "Lax"



# Désactiver JWT pour utiliser uniquement les sessions
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
}


ROOT_URLCONF = 'CocoaTraceProj.urls'

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

WSGI_APPLICATION = 'CocoaTraceProj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'cacaotracebd',
        'USER': 'postgres',
        'PASSWORD': 'baba237',
        'HOST': 'localhost',  #  l'adresse IP de votre serveur
        'PORT': '5432',  # port par défaut de PostgreSQL
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH_USER_MODEL = 'cocoaApp.User'

SESSION_COOKIE_AGE = 1209600  # Durée en secondes (ici, 2 semaines)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Efface la session à la fermeture du navigateur


import os

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "/build")  # Indiquer où sont les fichiers React
]
