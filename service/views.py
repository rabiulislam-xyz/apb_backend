from rest_framework import viewsets
from django_filters import rest_framework as filters

from service.filters import ServiceFilter
from service.models import Category, Service, CategoryType, FieldValue, FieldName, Area
from service.serializers import (
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategoryTypeSerializer,
    FieldValueSerializer,
    FieldNameSerializer,
    AreaSerializer,
    ServiceDetailSerializer,
    ServiceCreateSerializer,
)


class CategoryTypeViewSet(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoryDetailSerializer
        return CategoryListSerializer

    queryset = Category.objects.all()
    lookup_field = 'slug'


class ServiceViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            # return ServiceDetailSerializer
            return ServiceCreateSerializer
        return ServiceDetailSerializer

    queryset = Service.objects.all()
    lookup_field = 'slug'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ServiceFilter


class FieldNameViewSet(viewsets.ModelViewSet):
    queryset = FieldName.objects.all()
    serializer_class = FieldNameSerializer


class FieldValueViewSet(viewsets.ModelViewSet):
    queryset = FieldValue.objects.all()
    serializer_class = FieldValueSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
