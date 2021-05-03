from django.contrib import admin

from service.models import Service, Category, Image, CategoryType


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')
    search_fields = ('name', 'phone_number')


@admin.register(CategoryType)
class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'path')
    search_fields = ('title', )
