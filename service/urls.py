from django.urls import path, include
from rest_framework import routers

from service.views import CategoryViewSet, ServiceViewSet, CategoryTypeViewSet, FieldNameViewSet, FieldViewSet, \
    AddressViewSet

router = routers.DefaultRouter()
router.register(r'category_types', CategoryTypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'field_names', FieldNameViewSet)
router.register(r'fields', FieldViewSet)
router.register(r'locations', AddressViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
