from rest_framework import serializers

from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    qr_code = serializers.CharField(source='get_qr')
    class Meta:
        model = Goods
        fields = '__all__'
        depth = 1

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class GRSerializer(serializers.ModelSerializer):
    class Meta:
        model = GR
        fields = '__all__'
        depth = 2