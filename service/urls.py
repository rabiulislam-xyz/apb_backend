from django.urls import path, include
from rest_framework import routers

from service.views import CategoryViewSet, ServiceViewSet, CategoryTypeViewSet

router = routers.DefaultRouter()
router.register(r'category_types', CategoryTypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
