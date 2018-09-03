from django.contrib import admin

# Register your models here.

from . import models

# 注册model到admin中
admin.site.register(models.User)