from django.urls import path, include
from rest_framework import routers

from service.views import CategoryViewSet, ServiceViewSet, CategoryTypeViewSet, FieldNameViewSet, FieldValueViewSet, \
    AreaViewSet

router = routers.DefaultRouter()
router.register(r'category-types', CategoryTypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)
# router.register(r'field_names', FieldNameViewSet)
# router.register(r'field_values', FieldValueViewSet)
router.register(r'locations', AreaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
