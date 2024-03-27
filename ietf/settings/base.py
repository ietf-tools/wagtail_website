"""
Django settings for ietf project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf import global_settings

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Application definition

INSTALLED_APPS = (
    "ietf.home",
    "ietf.blog",
    "ietf.events",
    "ietf.search",
    "ietf.forms",
    "ietf.snippets",
    "ietf.standard",
    "ietf.topics",
    "ietf.glossary",
    "ietf.utils",
    "ietf.bibliography",
    "ietf.images",
    "ietf.documents",
    "ietf.iesg_statement",
    "ietf.announcements",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.contrib.search_promotions",
    "wagtail.admin",
    "wagtail",
    "wagtail.contrib.settings",
    "wagtail.contrib.table_block",
    "wagtail.contrib.routable_page",
    "wagtail_modeladmin",
    "wagtail.contrib.typed_table_block",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admindocs",
    "django.contrib.sitemaps",
    "analytical",
    "wagtailmarkdown",
    "wagtailorderable",
)

MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]


ROOT_URLCONF = "ietf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
                "ietf.context_processors.global_pages",
            ],
        },
    },
]

WSGI_APPLICATION = "ietf.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "ietf",
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, "static"),)

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# File upload permissions
# https://docs.djangoproject.com/en/3.2/ref/settings/#file-upload-permissions
FILE_UPLOAD_PERMISSIONS = 0o664


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "memcached:11211",
    },
    "sessions": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "memcached:11211",
    },
    "dummy": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"},
}


WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    },
}


WAGTAILMARKDOWN = {
    # We probably want to configure this more, see
    # https://github.com/torchbox/wagtail-markdown
    "autodownload_fontawesome": True,
}

# Wagtail settings

WAGTAIL_SITE_NAME = "ietf"
WAGTAIL_USAGE_COUNT_ENABLED = True
WAGTAILIMAGES_IMAGE_MODEL = "images.IETFImage"
WAGTAILDOCS_DOCUMENT_MODEL = "documents.IetfDocument"
WAGTAILADMIN_RICH_TEXT_EDITORS = {
    "default": {
        "WIDGET": "wagtail.admin.rich_text.DraftailRichTextArea",
        "OPTIONS": {
            "features": [
                "h2",
                "h3",
                "h4",
                "h5",
                "h6",
                "ol",
                "ul",
                "bold",
                "italic",
                "superscript",
                "subscript",
                "strikethrough",
                "hr",
                "link",
                "document-link",
                "image",
                "embed",
                "code",
                "blockquote",
            ]
        },
    }
}

# Application-wide settings
DATATRACKER_URI = "https://datatracker.ietf.org"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# IAB-specific subpage types.  When adding a new IAB subpage type, you'll need to update this.
IAB_SUBPAGE_TYPES = [
    "standard.IABStandardPage",
    "announcements.IABAnnouncementPage",
    "announcements.IABAnnouncementIndexPage",
]

IAB_PARENT_PAGE_TYPES = IAB_SUBPAGE_TYPES + [
    "home.IABHomePage",
]

IAB_FEED_URL = "https://www.ietf.org/blog/iab/feed"
IAB_IETF_BLOG_URL = "https://www.ietf.org/blog/iab/"

NOTE_WELL_REPO = "https://raw.githubusercontent.com/ietf/note-well/main/note-well.md"

_cf_purge_bearer_token = os.environ.get("CLOUDFLARE_CACHE_PURGE_BEARER_TOKEN")
_cf_purge_zone_id = os.environ.get("CLOUDFLARE_CACHE_PURGE_ZONE_ID")
if _cf_purge_bearer_token and _cf_purge_zone_id:  # pragma: no cover
    INSTALLED_APPS += ( "wagtail.contrib.frontend_cache", )
    WAGTAILFRONTENDCACHE = {
        "cloudflare": {
            "BACKEND": "wagtail.contrib.frontend_cache.backends.CloudflareBackend",
            "BEARER_TOKEN": _cf_purge_bearer_token,
            "ZONEID": _cf_purge_zone_id,
        },
    }
