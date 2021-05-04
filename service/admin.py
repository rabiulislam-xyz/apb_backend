from django.contrib import admin

from service.models import (
    Service,
    Category,
    CategoryFieldName,
    Image,
    CategoryType,
    Address,
    FieldName,
    Field)


# Services

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address', 'category', 'is_reviewed')
    search_fields = ('name', 'phone_number')
    list_filter = ('is_reviewed', )


# categories

@admin.register(CategoryType)
class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'type')


@admin.register(CategoryFieldName)
class CategoryFieldNameAdmin(admin.ModelAdmin):
    list_display = ('category', 'field_name', 'is_required')


# locations

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('area', 'word', 'city_corporation', 'slug')


# common

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'path')
    search_fields = ('title', )


@admin.register(FieldName)
class FieldNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name', )


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ('name', 'value')
