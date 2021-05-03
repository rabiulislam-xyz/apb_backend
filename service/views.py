from rest_framework import viewsets

from service.models import Category, Service, CategoryType
from service.serializers import CategoryListSerializer, CategoryDetailSerializer, ServiceSerializer, \
    CategoryTypeSerializer


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
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug'
