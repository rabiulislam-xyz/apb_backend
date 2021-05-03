from django.db import models

from core.utils import generate_slug


__all__ = ["CategoryType", "Category"]


class CategoryType(models.Model):
    name = models.CharField(max_length=200)

    slug = models.CharField(
        max_length=200,
        unique=True,
        null=True,
        blank=True)

    icon = models.ImageField(
        upload_to='icons/',
        null=True,
        blank=True)

    banner = models.ForeignKey(
        "service.Image",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='+')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category Types'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self, self.name)
        super().save(*args, **kwargs)


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


class Category(models.Model):
    name = models.CharField(max_length=200)

    slug = models.CharField(
        max_length=200,
        unique=True,
        null=True,
        blank=True)

    type = models.ForeignKey(
        "service.CategoryType",
        on_delete=models.PROTECT,
        related_name='categories')

    banner = models.ForeignKey(
        "service.Image",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='+')

    fields = models.ManyToManyField(
        to='service.FieldName',
        through='service.CategoryFieldName',
        related_name='+',
        blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self, self.name)
        super().save(*args, **kwargs)
