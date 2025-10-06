"""
Django settings for lista_compras project.
"""

from pathlib import Path
import os
import dj_database_url

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança
SECRET_KEY = 'django-insecure-quv=ej%r9g)i1u&25+!v6)kqi6$1oj62t(7h#s7%3g2np*o%^3'

# Debug: True localmente, False em produção
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Hosts permitidos
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'lista-compras-imqk.onrender.com']

# Host dinâmico para o Render
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Aplicações
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compras',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ Serve arquivos estáticos no Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lista_compras.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'lista_compras.wsgi.application'


# ==========================
# BANCO DE DADOS
# ==========================
if os.environ.get('DATABASE_URL'):  # Render define isso automaticamente
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:  # Local: SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# ==========================
# SENHAS
# ==========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==========================
# INTERNACIONALIZAÇÃO
# ==========================
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# ==========================
# ARQUIVOS ESTÁTICOS
# ==========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise: melhora performance e cache
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ==========================
# CONFIGURAÇÃO PADRÃO
# ==========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
