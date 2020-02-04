from rest_framework import serializers

from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    qr_code = serializers.CharField(source='get_qr', required=False)
    class Meta:
        model = Goods
        fields = '__all__'
        read_only_fields = ('sr_no', 'qr_code')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class GRSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True)
    class Meta:
        model = GR
        fields = '__all__'
        read_only_fields = ('gr_id',)
        

    def create(self, validated_data):
        goods = validated_data.pop('goods')
        instance = super(GRSerializer, self).create(validated_data)
        sr_index = 1
        for entry in goods:
            entry['sr_no'] = sr_index
            sr_index += 1
            saved_entry = Goods.objects.create(**entry)
            instance.goods.add(saved_entry.id)
        instance.save()
        return instance

        