from rest_framework import serializers
from .models import Favorite, Region, SubRegion, Category

class FavoriteSerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source='region.name', read_only=True)
    sub_region_name = serializers.CharField(source='sub_region.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    # receive primary keys for region, sub_region, and category
    region = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all())
    sub_region = serializers.PrimaryKeyRelatedField(queryset=SubRegion.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Favorite
        fields = [
            'id', 'name', 
            'region', 'region_name', 
            'sub_region', 'sub_region_name', 
            'category', 'category_name', 
            'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'region_name', 'sub_region_name', 'category_name']
