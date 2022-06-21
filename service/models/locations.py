from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.utils import generate_slug


__all__ = ["CityCorporationChoice", "Area"]


class CityCorporationChoice(models.TextChoices):
    BARISHAL = 'BARISHAL', _('Barishal')
    CHITTAGONG = 'CHITTAGONG', _('Chittagong')
    COMILLA = 'COMILLA', _('Comilla')
    DHAKA_NORTH = 'DHAKA_NORTH', _('Dhaka North')
    DHAKA_SOUTH = 'DHAKA_SOUTH', _('Dhaka South')
    GAZIPUR = 'GAZIPUR', _('Gazipur')
    NARAYANGANJ = 'NARAYANGANJ', _('Narayanganj')
    KHULNA = 'KHULNA', _('Khulna')
    MYMENSINGH = 'MYMENSINGH', _('Mymensingh')
    RAJSHAHI = 'RAJSHAHI', _('Rajshahi')
    RANGPUR = 'RANGPUR', _('Rangpur')
    SYLHET = 'SYLHET', _('Sylhet')


class Area(models.Model):
    name = models.CharField(max_length=255)
    word = models.PositiveSmallIntegerField(
        null=True,
        blank=True)

    city_corporation = models.CharField(
        null=True,
        blank=True,
        max_length=60,
        choices=CityCorporationChoice.choices)

    slug = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} word: {self.word or "all,"} {self.city_corporation or "all"} City Corporation'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self, self.name)
        super().save(*args, **kwargs)

    class Meta:
        # unique_together = (('word', 'city_corporation'), )
        ordering = ('word', )
