from django.contrib.auth import get_user_model
from django.db import models
from core.utils import generate_slug, phone_regex

User = get_user_model()

__all__ = ["Service"]


class Service(models.Model):
    name = models.CharField(
        max_length=300)

    slug = models.CharField(
        max_length=300,
        unique=True,
        null=True,
        blank=True)

    description = models.TextField(
        null=True,
        blank=True)

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17)

    category = models.ForeignKey(
        "service.Category",
        related_name='services',
        on_delete=models.PROTECT)

    address = models.ForeignKey(
        'service.Address',
        on_delete=models.PROTECT,
        related_name='services')

    images = models.ManyToManyField(
        'service.Image',
        related_name="+",
        blank=True)

    fields = models.ManyToManyField(
        to='service.Field',
        related_name='+',
        blank=True)

    is_reviewed = models.BooleanField(default=False)
    reviewed_by = models.ForeignKey(
        User,
        related_name='service_reviewed',
        on_delete=models.PROTECT,
        null=True,
        blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name='service_created',
        on_delete=models.PROTECT,
        null=True,
        blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        related_name='service_updated',
        on_delete=models.PROTECT,
        null=True,
        blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self, self.name)
        super().save(*args, **kwargs)
