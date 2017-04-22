# custom_storages.py
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

from django.core.files.storage import get_storage_class
from filebrowser_safe.storage import S3BotoStorageMixin

class StaticStorage(S3BotoStorage, S3BotoStorageMixin):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3BotoStorage, S3BotoStorageMixin):
    location = settings.MEDIAFILES_LOCATION

#class ThemeStorage(S3BotoStorage, S3BotoStorageMixin):
#    location = settings.THEMEFILES_LOCATION
