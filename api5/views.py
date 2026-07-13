from django.shortcuts import render
from rest_framework import viewsets
from api5.models import Products
from api5.serializers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer