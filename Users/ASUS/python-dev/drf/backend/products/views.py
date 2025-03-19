from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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


class ProductListApiView(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProducrSerializer

product_list_view = ProductListApiView.as_view()


@api_view(['GET','POST'])
def Product_alt_View(request, pk=None,*args, **kwargs):
  method = request.method
  if method == 'GET':
    if pk is not None:
      #detail view
      obj = get_object_or_404(Product,pk=pk)
      data = ProducrSerializer(obj,many=False).data
      return Response(data)
    
    #URL's args
    #get request detail view
    #list view

    queryset = Product.objects.all()
    data = ProducrSerializer(queryset,many=True).data
    return Response(data)
  if method == 'POST':
    #Create New Methods
    serializer = ProducrSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None: 
          content = title
        serializer.save(content=content)
        return Response(serializer.data)
    return Response({"Not valid"},status=400)

