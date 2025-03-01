from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models


@admin.register(models.Post)
class CustomAdminClass(ModelAdmin):
    pass
