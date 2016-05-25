import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'bustimes.org.uk').split()

DEBUG = bool(os.environ.get('DEBUG', False))

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'haystack',
    'busstops',
    'pipeline',
)

ROOT_URLCONF = 'buses.urls'

MIDDLEWARE_CLASSES = (
    'busstops.middleware.NotFoundRedirectMiddleware',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    } if DEBUG else {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
HAYSTACK_IDENTIFIER_METHOD = 'buses.utils.get_identifier'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'NAME': os.environ.get('DATABASE_NAME', 'bustimes'),
    },
}

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', '/home/josh/bustimes-static/')
if DEBUG:
    STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
else:
    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
PIPELINE = {
    'COMPILERS': [
        'pipeline.compilers.sass.SASSCompiler',
    ],
    'STYLESHEETS': {
        'main': {
            'source_filenames': (
                'css/style.scss',
            ),
            'output_filename': 'css/style.css',
        },
        'ie': {
            'source_filenames': (
                'css/ie.scss',
            ),
            'output_filename': 'css/ie.css',
        }
    },
    'JAVASCRIPT': {
        'frontpage': {
            'source_filenames': (
                'js/frontpage.js',
            ),
            'output_filename': 'js/frontpage.min.js',
        },
    },
    'YUGLIFY_BINARY': './node_modules/.bin/yuglify',
    'CSS_COMPRESSOR': None,
    'SASS_ARGUMENTS': '--style compressed --trace',
}

TEMPLATE_MINIFER_STRIP_FUNCTION = 'buses.utils.minify'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'loaders': (
                ('django.template.loaders.cached.Loader', (
                    'template_minifier.template.loaders.app_directories.Loader',
                )),
            ),
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
            )
        }
    }
]

TIME_FORMAT = 'H:i'
DATE_FORMAT = 'j F Y'
TIME_ZONE = 'Europe/London'
USE_I18N = False

TRANSPORTAPI_APP_ID = os.environ.get('TRANSPORTAPI_APP_ID')
TRANSPORTAPI_APP_KEY = os.environ.get('TRANSPORTAPI_APP_KEY')