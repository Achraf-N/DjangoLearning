from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProducrSerializer

# Create your views here.

class ProductDetailApiView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProducrSerializer

product_detail_view = ProductDetailApiView.as_view()


class ProductCreateApiView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProducrSerializer

  def perform_create(self,serializer):
    print(serializer.validated_data)
    title = serializer.validated_data.get("title")
    content = serializer.validated_data.get("content")
    serializer.save() or None 
    if content is None: 
      content = title
    serializer.save(content=content)

product_create_view = ProductCreateApiView.as_view()