from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from datetime import datetime, timedelta
# import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iyk(1r341s2zm*w@z5s*t8u6e)wn^78b9a3_qs-%gy4u&yfukm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
   # ...
   '127.0.0.1',
   # ...
]

# Application definition
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


TIERS_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    'import_export',
    'crispy_forms',
    'taggit',

    'embed_video',
    'django_ckeditor_5',
    
    'parler',

    'debug_toolbar',
    'whitenoise.runserver_nostatic',
]

AUTERS_APPS = [
    'webapp',
]

import os

# Liste des dossiers à exclure
excluded_folders = ['static', 'media', 'templates', 'locale', 'logs', 'api_rest', ]
excluded_folders += AUTERS_APPS

# Chemin du répertoire racine du projet
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Liste des dossiers à inclure dans PROJECT_APPS
PROJECT_APPS = []

# Parcourir les dossiers dans le répertoire racine
for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)
    # Vérifier si le dossier n'est pas dans la liste des exclusions et est un dossier (pas un fichier)
    if folder not in excluded_folders and os.path.isdir(folder_path):
        # Ajouter le nom du dossier à PROJECT_APPS
        PROJECT_APPS.append(folder)

INSTALLED_APPS = DEFAULT_APPS + TIERS_APPS + PROJECT_APPS + AUTERS_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.locale.LocaleMiddleware', #langue
    'debug_toolbar.middleware.DebugToolbarMiddleware', #new
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'api_rest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath("templates"))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n', #langue
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

WSGI_APPLICATION = 'api_rest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('DB_NAME'), #here
#         'USER': os.environ.get('DB_USER'), #here
#         'PASSWORD': os.environ.get('DB_PASS'), #here
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', 'Anglais'),
    ('fr', 'Français'),
]

LOCALE_PATHS = [
os.path.join(BASE_DIR, 'locale'),
]

# Configuration de PARLER_LANGUAGES
PARLER_LANGUAGES = {
    # Langue par défaut
    None: [
        {
            'code': 'fr',
            'name': 'Français',
            'fallbacks': ['en'],
        },
        {
            'code': 'en',
            'name': 'English',
            'fallbacks': ['fr'],
        },
    ],
    # Autres langues prises en charge
    'default': {
        'fallback': 'fr',
        'hide_untranslated': False,
    },
    'languages': [
        {
            'code': lang_code,
            'name': dict(LANGUAGES)[lang_code],
            'fallbacks': ['fr', 'en'],
        } for lang_code, lang_name in LANGUAGES
    ]
}

PARLER_DEFAULT_LANGUAGE_CODE = 'fr'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

customColorPalette = [
        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
        },
        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
        },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
        },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
        },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
        },
        {
            'color': 'hsl(207, 90%, 54%)',
            'label': 'Blue'
        },
    ]

# CKEDITOR_5_CUSTOM_CSS = 'path_to.css' # optional
# CKEDITOR_5_FILE_STORAGE = "path_to_storage.CustomStorage" # optional
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# White listing the localhost:3000 port
# for React
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://localhost:8080',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

CORS_ORIGIN_ALLOW_ALL = True

# custome user modele
# AUTH_USER_MODEL = 'authentification.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGIN_REDIRECT_URL = "index"
ACCOUNT_LOGOUT_ON_GET = True

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Messages Configuration
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


# logs
import os
from datetime import datetime

# Configure logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'logs')

def log_file_path(log_type):
    current_date = datetime.now().strftime("%Y%m%d")
    log_type_dir = os.path.join(LOG_DIR, current_date)
    if not os.path.exists(log_type_dir):
        os.makedirs(log_type_dir)
    return os.path.join(log_type_dir, f"{log_type}.log")

# ...

# Other Django settings
# ...

# Configuration pour enregistrer les logs dans des fichiers séparés par type
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': log_file_path('debug'),
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': log_file_path('error'),
        },
        'info_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': log_file_path('info'),
        },
    },
    'loggers': {
        'debug_logger': {
            'handlers': ['debug_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'error_logger': {
            'handlers': ['error_file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'info_logger': {
            'handlers': ['info_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


