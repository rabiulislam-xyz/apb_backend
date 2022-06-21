from django_filters import rest_framework as filters

from service.models import Service


class ServiceFilter(filters.FilterSet):
    class Meta:
        model = Service
        fields = [
            'category__slug',
            'area__word',
            'area__city_corporation'
        ]
