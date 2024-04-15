from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rw7%0^777yj5=^1pd3#1r9t_@0dqtighks8uzf&5y+ach(0_&o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Ensure that all HTTP requests are redirected to HTTPS
SECURE_SSL_REDIRECT = True


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'connect.apps.ConnectConfig',
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

ROOT_URLCONF = 'comrade.urls'

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

WSGI_APPLICATION = 'comrade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'comradeconnectdb',  # Your MySQL database name
        'USER': 'root',       # Your MySQL username
        'PASSWORD': '',   # Your MySQL password
        'HOST': 'localhost',                    # Your MySQL host (usually 'localhost' for local installations)
        'PORT': '5432',                         # Use the default PostgreSQL port
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
import os

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'

# App-level static files
APP_STATIC_ROOT = os.path.join(BASE_DIR, 'connect/static')
STATICFILES_DIRS = [APP_STATIC_ROOT]

#Project level static files
# Absolute filesystem path to the directory that will hold collected static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'comrade/static'),
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
