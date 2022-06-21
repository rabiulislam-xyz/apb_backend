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

    sorting_id = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        unique=True, 
        help_text='Value for ordering/sorting list, lower is high priority')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category Types'
        ordering = ('sorting_id', 'name')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self, self.name)
        super().save(*args, **kwargs)


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

    field_names = models.ManyToManyField(
        to='service.FieldName',
        through='service.CategoryFieldName',
        related_name='+',
        blank=True)

    sorting_id = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        unique=True, 
        help_text='Value for ordering/sorting list, lower is high priority')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('sorting_id', 'name')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self, self.name)
        super().save(*args, **kwargs)
