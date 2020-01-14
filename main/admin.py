from django.contrib import admin
from .models import Users, statistics, removeMe, mediaFiles

# Register your models here.

admin.site.register(Users)
admin.site.register(statistics)
admin.site.register(removeMe)
admin.site.register(mediaFiles)
