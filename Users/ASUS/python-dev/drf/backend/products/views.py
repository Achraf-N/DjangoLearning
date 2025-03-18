from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProducrSerializer

# Create your views here.

class ProductDetailApiView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProducrSerializer

product_detail_view = ProductDetailApiView.as_view()