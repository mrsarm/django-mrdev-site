# -*- coding: utf-8 -*-
##############################################################################
#
#    MRDEV Site - Django CMS
#    Copyright (C) 2014 MRDEV Software (<http://mrdev.com.ar>).
#
#    Django settings for mrdev project.
#
#    For more information on this file, see
#    https://docs.djangoproject.com/en/1.5/topics/settings/
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import re

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

gettext = lambda s: s


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ffeettyy66pp@@111111111111111111112222222222!!!!x@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'reversion',
    'djangocms_text_ckeditor',
    'cms.plugins.flash',
    'cms.plugins.googlemap',

    # Django-Filer
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    #'cms.plugins.file',
    #'cms.plugins.picture',
    #'cms.plugins.teaser',
    #'cms.plugins.video',

    'bootstrap3',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'common_context.context_processors.site',
    'common_context.context_processors.settings',
)

THUMBNAIL_PROCESSORS = (
    # Django-Filer processors
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

#FILER_IMAGE_USE_ICON=True

# Django-Filer integration with djangocms-text-ckeditor
TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

ROOT_URLCONF = 'mrdev.urls'

WSGI_APPLICATION = 'mrdev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'django_mrdev.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_mrdev',
        'USER': 'django',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_ROOT = os.path.join(PROJECT_PATH, "static")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_PATH, "static")
#MEDIA_URL = "/media/"

STATICFILES_IGNORE_DEBUG=True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATICFILES_DIRS = (MEDIA_ROOT,)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

LANGUAGES = (
    ('es', gettext('Spanish')),
    ('en', gettext('English')),
)

CMS_LANGUAGES = (
    ('es', gettext('Spanish')),
    ('en', gettext('English')),
)

LOCALE_INDEPENDENT_PATHS = (
    re.compile('^%s' % STATIC_URL),
)

# Language fallback ordering for each language
#CMS_HIDE_UNTRANSLATED=False
#CMS_LANGUAGE_FALLBACK=True
#CMS_LANGUAGE_CONF = {
#    'en': ['es'],
#}

TEMPLATE_DIRS = (
    # The docs say it should be absolute path: PROJECT_PATH is precisely one.
    # Life is wonderful!
    os.path.join(PROJECT_PATH, "templates"),
)

CMS_TEMPLATES = (
    ('mrdev/bootstrap3/jumbotron/jumbotron-narrow-1.html', gettext('Bootstrap3 Jumbotron Narrow')),
    ('mrdev/bootstrap3/jumbotron/jumbotron-narrow-2.html', gettext('Bootstrap3 Jumbotron Narrow 2 Columns')),
    ('mrdev/bootstrap3/jumbotron/jumbotron-narrow-2-25-75.html', gettext('Bootstrap3 Jumbotron Narrow 2 Columns (25-75)')),
    ('mrdev/bootstrap3/jumbotron/jumbotron-narrow-2-75-25.html', gettext('Bootstrap3 Jumbotron Narrow 2 Columns (75-25)')),
    ('mrdev/bootstrap3/jumbotron/jumbotron-narrow-3.html', gettext('Bootstrap3 Jumbotron Narrow 3 Columns')),
)

CMS_PLACEHOLDER_CONF = {
    'js': {
        'plugins': ('SnippetPlugin'),
        'name': gettext("JavaScript"),
    },
    'css': {
        'plugins': ('SnippetPlugin'),
        'name': gettext("CSS Style"),
    },
    'top':    { 'name': gettext("Top"), },
    'bottom': { 'name': gettext("Bottom"), },
    'sidebar': { 'name': gettext("Sidebar"), },
    'main':   { 'name': gettext("Main"), },
    'main-2': { 'name': gettext("Main") + " 2", },
    'main-3': { 'name': gettext("Main") + " 3", },
}


#CMS_UNIHANDECODE_HOST=True
#CMS_UNIHANDECODE_VERSION=True

# Site ID, after install, or rename from Admin Panel:
#     UPDATE django_site SET name = 'MRDEV Site', domain = 'www.mrdev.com.ar';
SITE_ID=1

CMS_PERMISSION=True


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers':['console', 'logfile'],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['console', 'logfile','mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'mrdev.custom': {
            'handlers': ['console', 'logfile', 'mail_admins'],
            'level': 'INFO',
        }
    }
}
