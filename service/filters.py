from django_filters import rest_framework as filters

from service.models import Service


class ServiceFilter(filters.FilterSet):
    class Meta:
        model = Service
        fields = [
            'category__slug',
            'address__word',
            'address__city_corporation'
        ]
