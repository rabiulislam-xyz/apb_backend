from rest_framework import serializers

from service.models import Category, Service, Image, CategoryType


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'path', 'description', 'image']


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            'category': {'lookup_field': 'slug'},
        }


class CategoryListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='category-detail',
        lookup_field='slug',
    )

    class Meta:
        model = Category
        fields = ['name', 'slug', 'url']
        lookup_field = 'slug'


class CategoryTypeMiniSerializer(serializers.ModelSerializer):
    banner = ImageSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='categorytype-detail',
        lookup_field='slug',
    )

    class Meta:
        model = CategoryType
        fields = ['name', 'slug', 'banner', 'url']
        lookup_field = 'slug'


class CategoryDetailSerializer(serializers.ModelSerializer):
    banner = ImageSerializer(read_only=True)
    type = CategoryTypeMiniSerializer(read_only=True)
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'slug', 'banner', 'type', 'services']
        lookup_field = 'slug'


class CategoryTypeSerializer(serializers.ModelSerializer):
    banner = ImageSerializer(read_only=True)
    categories = CategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = CategoryType
        fields = ['name', 'slug', 'banner', 'icon', 'categories']
        lookup_field = 'slug'
