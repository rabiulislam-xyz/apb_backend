import logging

from rest_framework import serializers

from service.models import Category, Service, Image, CategoryType, FieldValue, FieldName, Area

logger = logging.getLogger(__name__)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'path', 'description', 'image')
        read_only_fields = ('id',)


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name', 'word', 'city_corporation')
        read_only_fields = ('id', )


class FieldNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldName
        fields = ('id', 'name', 'type')
        read_only_fields = ('id',)


class FieldValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldValue
        fields = ('id', 'name', 'value')
        read_only_fields = ('id',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = FieldNameSerializer(instance.name).data
        return data


class CategoryListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='category-detail',
        lookup_field='slug',
    )

    class Meta:
        model = Category
        fields = ('name', 'slug', 'url', 'icon')
        lookup_field = 'slug'


class ServiceDetailSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    area = AreaSerializer()
    field_values = FieldValueSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = (
            'created_by', 'created_at',
            'updated_by', 'updated_at'
        )
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            'category': {'lookup_field': 'slug'},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        fields = (
            'reviewed_by', 'created_by', 'created_at',
            'updated_by', 'updated_at'
        )
        representation['meta'] = {f: representation[f] for f in fields}

        for f in fields:
            del representation[f]

        return representation


class ServiceMiniSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    area = AreaSerializer()

    class Meta:
        model = Service
        fields = (
            'name', 'slug', 'description', 'phone_number',
            'address', 'images', 'area'
        )
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = (
            'created_by', 'created_at',
            'updated_by', 'updated_at'
        )
        lookup_field = 'slug'

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        validated_data['updated_by'] = self.context['request'].user
        return super().create(validated_data)


class CategoryTypeMiniSerializer(serializers.ModelSerializer):
    banner = ImageSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='categorytype-detail',
        lookup_field='slug',
    )

    class Meta:
        model = CategoryType
        fields = ('name', 'slug', 'banner', 'url')
        lookup_field = 'slug'


class CategoryDetailSerializer(serializers.ModelSerializer):
    banner = ImageSerializer(read_only=True)
    type = CategoryTypeMiniSerializer(read_only=True)
    fields = FieldNameSerializer(many=True, read_only=True)
    services = ServiceMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'banner', 'type', 'icon', 'fields', 'services')
        lookup_field = 'slug'


class CategoryTypeSerializer(serializers.ModelSerializer):
    banner = ImageSerializer(read_only=True)
    categories = CategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = CategoryType
        fields = ('name', 'slug', 'banner', 'icon', 'categories')
        lookup_field = 'slug'
