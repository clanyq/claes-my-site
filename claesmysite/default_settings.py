import os

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

COMPRESS_OFFLINE = False

COMPRESS_OUTPUT_DIR = ''

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'sassc {infile} {outfile}'),
    ('text/jsx', 'NODE_ENV=production node_modules/.bin/browserify -t reactify {infile} -o {outfile}'),
)

try:
    from .local_settings import *
except ImportError:
    pass

if settings.DEBUG == False:
    COMPRESS_OFFLINE = True
    COMPRESS_PRECOMPILERS = (
        ('text/x-scss', 'sassc {infile} {outfile}'),
        ('text/jsx', 'NODE_ENV=production node_modules/.bin/browserify -t reactify {infile} | node_modules/.bin/uglifyjs -cm > {outfile}'),
    )