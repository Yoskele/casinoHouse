from rest_framework import serializers
from .models import ArticlePost, Casino, GameSupplier


class ArticlePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlePost
        fields = '__all__'
        lookup_field = 'slug'


class CasinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casino
        fields = '__all__'
        lookup_field = 'slug'


class GameSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSupplier
        fields = '__all__'
        lookup_field = 'slug'
