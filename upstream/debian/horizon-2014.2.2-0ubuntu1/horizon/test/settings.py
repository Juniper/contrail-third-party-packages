# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import socket
import sys

import django
from django.utils import html_parser
import horizon.xstatic.main
import horizon.xstatic.pkg.angular
import horizon.xstatic.pkg.angular_cookies
import horizon.xstatic.pkg.angular_mock
import horizon.xstatic.pkg.bootstrap_datepicker
import horizon.xstatic.pkg.bootstrap_scss
import horizon.xstatic.pkg.d3
import horizon.xstatic.pkg.font_awesome
import horizon.xstatic.pkg.hogan
import horizon.xstatic.pkg.jasmine
import horizon.xstatic.pkg.jquery
import horizon.xstatic.pkg.jquery_migrate
import horizon.xstatic.pkg.jquery_quicksearch
import horizon.xstatic.pkg.jquery_tablesorter
import horizon.xstatic.pkg.jquery_ui
import horizon.xstatic.pkg.jsencrypt
import horizon.xstatic.pkg.qunit
import horizon.xstatic.pkg.rickshaw
import horizon.xstatic.pkg.spin

from horizon.test import patches

# Patch django.utils.html_parser.HTMLParser as a workaround for bug 1273943
if django.get_version() == '1.4' and sys.version_info[:3] > (2, 7, 3):
    html_parser.HTMLParser.parse_starttag = patches.parse_starttag_patched

socket.setdefaulttimeout(1)

LOGIN_URL = '/auth/login/'
LOGOUT_URL = '/auth/logout/'
LOGIN_REDIRECT_URL = '/'

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DEBUG = False
TEMPLATE_DEBUG = DEBUG
TESTSERVER = 'http://testserver'

SECRET_KEY = 'elj1IWiLoWHgcyYxFVLj7cM5rGOOxWl0'

USE_I18N = True
USE_L10N = True
USE_TZ = True

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

DEFAULT_EXCEPTION_REPORTER_FILTER = 'horizon.exceptions.HorizonReporterFilter'

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_nose',
    'django_pyscss',
    'compressor',
    'horizon',
    'horizon.test',
    'horizon.test.test_dashboards.cats',
    'horizon.test.test_dashboards.dogs'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'horizon.middleware.HorizonMiddleware')

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'horizon.context_processors.horizon')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'horizon.loaders.TemplateLoader'
)

STATIC_URL = '/static/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

ROOT_URLCONF = 'horizon.test.urls'
TEMPLATE_DIRS = (os.path.join(ROOT_PATH, 'tests', 'templates'),)
SITE_ID = 1
SITE_BRANDING = 'Horizon'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--nocapture',
             '--nologcapture',
             '--exclude-dir=horizon/conf/',
             '--exclude-dir=horizon/test/customization',
             '--cover-package=horizon',
             '--cover-inclusive',
             '--all-modules']

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECURE = False

HORIZON_CONFIG = {
    'dashboards': ('cats', 'dogs'),
    'default_dashboard': 'cats',
    "password_validator": {
        "regex": '^.{8,18}$',
        "help_text": "Password must be between 8 and 18 characters."
    },
    'user_home': None,
    'help_url': "http://example.com",
}

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_ROOT = "/tmp/"
COMPRESS_PARSER = 'compressor.parser.HtmlParser'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = [
    ('horizon/lib/angular',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.angular).base_dir),
    ('horizon/lib/angular',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.angular_cookies).base_dir),
    ('horizon/lib/angular',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.angular_mock).base_dir),
    ('horizon/lib/bootstrap_datepicker',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.bootstrap_datepicker).base_dir),
    ('bootstrap',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.bootstrap_scss).base_dir),
    ('horizon/lib',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.d3).base_dir),
    ('horizon/lib',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.hogan).base_dir),
    ('horizon/lib/font-awesome',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.font_awesome).base_dir),
    ('horizon/lib/jasmine-1.3.1',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.jasmine).base_dir),
    ('horizon/lib/jquery',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.jquery).base_dir),
    ('horizon/lib/jquery',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.jquery_migrate).base_dir),
    ('horizon/lib/jquery',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.jquery_quicksearch).base_dir),
    ('horizon/lib/jquery',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.jquery_tablesorter).base_dir),
    ('horizon/lib/jsencrypt',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.jsencrypt).base_dir),
    ('horizon/lib/qunit',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.qunit).base_dir),
    ('horizon/lib',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.rickshaw).base_dir),
    ('horizon/lib',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.spin).base_dir),
]

if horizon.xstatic.main.XStatic(horizon.xstatic.pkg.jquery_ui).version.startswith('1.10.'):
    # The 1.10.x versions already contain the 'ui' directory.
    STATICFILES_DIRS.append(('horizon/lib/jquery-ui',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.jquery_ui).base_dir))
else:
    # Newer versions dropped the directory, add it to keep the path the same.
    STATICFILES_DIRS.append(('horizon/lib/jquery-ui/ui',
        horizon.xstatic.main.XStatic(horizon.xstatic.pkg.jquery_ui).base_dir))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'test': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
        },
        'horizon': {
            'handlers': ['test'],
            'propagate': False,
        },
        'nose.plugins.manager': {
            'handlers': ['null'],
            'propagate': False,
        },
        'selenium': {
            'handlers': ['null'],
            'propagate': False,
        }
    }
}
