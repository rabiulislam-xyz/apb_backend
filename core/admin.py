from django.contrib import admin
from django.contrib.auth.models import Permission

from core.models import User


@admin.register(User)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    search_fields = ('codename', 'name')
    list_filter = ['content_type']
    list_display = ['__str__', 'content_type', 'codename', 'name']
