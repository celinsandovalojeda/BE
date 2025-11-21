from pathlib import Path
from datetime import timedelta

# =========================
# BASE DIR
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# CONFIG BÁSICA
# =========================
SECRET_KEY = 'dev'
DEBUG = True
ALLOWED_HOSTS = ['*']  # ← necesario para EC2


# =========================
# INSTALLED APPS
# =========================
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Filtros
    'django_filters',

    # Swagger
    'drf_yasg',

    # DRF
    'rest_framework',

    # JWT
    'rest_framework_simplejwt',

    # CORS
    'corsheaders',

    # Apps del proyecto
    'transporte',     # backend
    # Si tuvieras un app frontend, iría aquí
]


# =========================
# MIDDLEWARE
# =========================
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


# =========================
# CORS
# =========================
CORS_ALLOW_ALL_ORIGINS = True


# =========================
# URLS
# =========================
ROOT_URLCONF = 'logistica.urls'


# =========================
# TEMPLATES (FRONTEND B)
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "transporte" / "templates",   # TUS TEMPLATES BOOTSTRAP
        ],
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


# =========================
# WSGI
# =========================
WSGI_APPLICATION = 'logistica.wsgi.application'


# =========================
# BASE DE DATOS (LOCAL)
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'logistica_bd2',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}


# =========================
# VALIDACIÓN DE PASSWORD
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =========================
# IDIOMA Y ZONA HORARIA
# =========================
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True


# =========================
# STATIC
# =========================
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "transporte" / "static",
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================
# DJANGO REST FRAMEWORK
# =========================
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


# =========================
# JWT (BACKEND)
# =========================
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}


# =========================
# SWAGGER
# =========================
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Bearer <token>',
        }
    },
    'USE_SESSION_AUTH': False,
}