SECRET_KEY = "dev"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "logistica",
]

MIDDLEWARE = []

ROOT_URLCONF = "frontend_demo.urls"

STATIC_URL = "/static/"
STATICFILES_DIRS = []

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]

WSGI_APPLICATION = "frontend_demo.wsgi.application"
