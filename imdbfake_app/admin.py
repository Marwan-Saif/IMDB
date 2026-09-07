from django.contrib import admin

from imdbfake_app.models import StreamPlatform, WatchList

# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamPlatform)