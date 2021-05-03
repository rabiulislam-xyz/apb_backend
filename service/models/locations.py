from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.utils import generate_slug


__all__ = ["CityCorporationChoice", "Address"]


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


class Address(models.Model):
    area = models.CharField(max_length=255)
    word = models.PositiveSmallIntegerField()

    city_corporation = models.CharField(
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
        return f'{self.area} word: {self.word} {self.city_corporation} City Corporation'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self, self.city_corporation)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = (('word', 'city_corporation'), )
