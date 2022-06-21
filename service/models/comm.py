from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = ["Image", "AttributeTypeChoice", "FieldName", "CategoryFieldName", "FieldValue"]


class Image(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    path = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AttributeTypeChoice(models.TextChoices):
    TEXT = 'TEXT', _('Text')
    RICH_TEXT = 'RICH_TEXT', _('Rich Text')
    NUMBER = 'NUMBER', _('Number')
    BOOLEAN = 'BOOLEAN', _('Boolean')
    DATE = 'DATE', _('Date')
    URL = 'URL', _('Url')
    PHONE = 'PHONE', _('Phone Number')


class FieldName(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=30,
        choices=AttributeTypeChoice.choices,
        default=AttributeTypeChoice.TEXT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CategoryFieldName(models.Model):
    """
    Through table for store is_required value
    """
    category = models.ForeignKey(
        'service.Category',
        related_name='+',
        on_delete=models.CASCADE)

    field_name = models.ForeignKey(
        'service.FieldName',
        related_name='+',
        on_delete=models.CASCADE)

    is_required = models.BooleanField(default=True)


class FieldValue(models.Model):
    name = models.ForeignKey(
        'service.FieldName',
        related_name='+',
        on_delete=models.PROTECT)

    value = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.value}"
