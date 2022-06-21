from django.contrib import admin

from service.models import (
    Service,
    Category,
    Image,
    CategoryType,
    Area,
    FieldName,
    CategoryFieldName,
    FieldValue,
)


# Services

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'area', 'category', 'is_reviewed', 'sorting_id')
    search_fields = ('name', 'phone_number')
    list_filter = ('is_reviewed', )


# categories

@admin.register(CategoryType)
class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'sorting_id')
    search_fields = ('name', )


class CategoryFieldNameInline(admin.TabularInline):
    model = CategoryFieldName
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'type', 'sorting_id')
    search_fields = ('name', )
    inlines = (CategoryFieldNameInline, )


@admin.register(CategoryFieldName)
class CategoryFieldNameAdmin(admin.ModelAdmin):
    list_display = ('category', 'field_name', 'is_required')


# locations

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'word', 'city_corporation', 'slug')


# common

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'path')
    search_fields = ('title', )


@admin.register(FieldName)
class FieldNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    search_fields = ('name', )


@admin.register(FieldValue)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ('name', 'value')
