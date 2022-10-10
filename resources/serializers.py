from . models import CoffeTypes, Shop
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeTypes
        fields = ('name', )


class ShopSerializer(GeoFeatureModelSerializer):
    type_of_coffe = TypeSerializer(many=True)

    class Meta:
        model = Shop
        geo_field = "location"
        fields = ('name', 'type_of_coffe', 'street_name')
