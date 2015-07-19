# -*- coding: utf-8 -*-
##############################################################################
#
#    MRDEV Site - Django CMS
#    Copyright (C) 2014 MRDEV Software (<http://mrdev.com.ar>).
#
#    Django settings for mrdev project.
#
#    For more information on this file, see
#    https://docs.djangoproject.com/en/1.8/topics/settings/
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

#from django.utils.translation import ugettext_lazy as _
_ = lambda s: s


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ffeettyy66pp@@111111111111111111112222222222!!!!x@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'admin_shortcuts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'reversion',
    #'djangocms_link',
    #'djangocms_snippet',
    'djangocms_style',
    'djangocms_column',
    'djangocms_inherit',
    'djangocms_flash',
    #'djangocms_googlemap',
    #'djangocms_teaser',
    #'djangocms_video',

    # Django-Filer
    'filer',
    'easy_thumbnails',
    #'cmsplugin_filer_file',
    #'cmsplugin_filer_folder',
    #'cmsplugin_filer_link',
    #'cmsplugin_filer_image',
    #'cmsplugin_filer_teaser',
    #'cmsplugin_filer_video',

    #'cmsplugin_filery',
    #'cmsplugin_nivoslider',

    'bootstrap3',
    #'cmsplugin_contact',
    'mrdev'
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mrdev', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings',
                'common_context.context_processors.site',
                'common_context.context_processors.settings',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

THUMBNAIL_PROCESSORS = (
    # Django-Filer processors
    'easy_thumbnails.processors.colorspace',
    #'cmsplugin_nivoslider.thumbnail_processors.pad_image',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_HIGH_RESOLUTION = True

#FILER_IMAGE_USE_ICON=True

# Django-Filer integration with djangocms-text-ckeditor
TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

ROOT_URLCONF = 'mrdev.urls'

WSGI_APPLICATION = 'mrdev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'project.sqlite3'),
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'django_mrdev',
        #'USER': 'django',
        #'PASSWORD': 'postgres',
        #'HOST': 'localhost',
        #'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_PATH, "static")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"

STATICFILES_IGNORE_DEBUG=True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es'

#USE_TZ = True  # Default False
#TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Buenos_Aires'

USE_I18N = True

USE_L10N = True

LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English')),
)

CMS_LANGUAGES = {
    1: [
        {
            'code': 'es',
            'name': _('Spanish'),
            'fallbacks': ['en'],
        },
        {
            'code': 'en',
            'name': _('English'),
            'fallbacks': ['es'],
        },
    ],
    'default': {
        'fallbacks': ['es', 'en'],
        'redirect_on_fallback':True,
        'public': True,
        'hide_untranslated': False,
    }
}

LOCALE_INDEPENDENT_PATHS = (
    re.compile('^%s' % STATIC_URL),
    re.compile('^%s' % MEDIA_URL),
)

# Language fallback ordering for each language
#CMS_HIDE_UNTRANSLATED=False
#CMS_LANGUAGE_FALLBACK=True
#CMS_LANGUAGE_CONF = {
#    'en': ['es'],
#}

CMS_TEMPLATES = (
    ('mrdev/bootstrap3/jumbotron/jumbotron-narrow-1.html', _('Bootstrap3 Jumbotron Narrow')),
    ('mrdev/bootstrap3/jumbotron/jumbotron-narrow-2.html', _('Bootstrap3 Jumbotron Narrow 2 Columns')),
    ('mrdev/bootstrap3/jumbotron/jumbotron-narrow-2-25-75.html', _('Bootstrap3 Jumbotron Narrow 2 Columns (25-75)')),
    ('mrdev/bootstrap3/jumbotron/jumbotron-narrow-2-75-25.html', _('Bootstrap3 Jumbotron Narrow 2 Columns (75-25)')),
    ('mrdev/bootstrap3/jumbotron/jumbotron-narrow-3.html', _('Bootstrap3 Jumbotron Narrow 3 Columns')),
)

CMS_PLACEHOLDER_CONF = {
    'js': {
        'plugins': ('SnippetPlugin'),
        'name': _("JavaScript"),
    },
    'css': {
        'plugins': ('SnippetPlugin'),
        'name': _("CSS Style"),
    },
    'top':    { 'name': _("Top"), },
    'bottom': { 'name': _("Bottom"), },
    'sidebar': { 'name': _("Sidebar"), },
    'main':   { 'name': _("Main"), },
    'main-2': { 'name': _("Main") + " 2", },
    'main-3': { 'name': _("Main") + " 3", },
}

BOOTSTRAP3 = {
    'css_url': '/static/bootstrap3/sandstone/bootstrap.min.css',
    'javascript_url': '/static/bootstrap3/js/bootstrap.min.js',
}


#CMS_UNIHANDECODE_HOST=True
#CMS_UNIHANDECODE_VERSION=True

# Site ID, after install, or rename from Admin Panel:
#     UPDATE django_site SET name = 'MRDEV Site', domain = 'www.mrdev.com.ar';
SITE_ID=1

CMS_PERMISSION=True

"""
Email conf
"""
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'userxxx@gmail.com'
EMAIL_HOST_PASSWORD = 'passxxx'
EMAIL_PORT = 587
EMAIL_FROM = 'No-Reply'
EMAIL_REPPLY = ''

DEFAULT_FROM_EMAIL = 'No-Reply <userxxx@gmail.com>'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/1.8/topics/logging for
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

ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            {
                'url': '/',
                'open_new_window': True,
            },
            {
                'url_name': 'admin:cms_page_changelist',
                'title': _('Pages'),
            },
            {
                'url_name': 'admin:filer_folder_changelist',
                'title': _('Files'),
            },
            {
                'url_name': 'admin:auth_user_changelist',
                'title': _('Users'),
            },
        ]
    },
]

MIGRATION_MODULES = {
    'filer': 'filer.migrations_django',
    'djangocms_column': 'djangocms_column.migrations_django',
    #'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    #'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    #'djangocms_link': 'djangocms_link.migrations_django',
    #'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
    #'djangocms_teaser': 'djangocms_teaser.migrations_django',
    #'djangocms_video': 'djangocms_video.migrations_django',
    #'djangocms_snippet': 'djangocms_snippet.migrations_django',

    #'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    #'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    #'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
    #'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    #'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    #'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
}
