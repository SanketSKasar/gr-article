from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *

class GRViewSet(viewsets.ModelViewSet):
    queryset = GR.objects.all()
    serializer_class = GRSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer