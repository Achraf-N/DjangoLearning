from rest_framework import serializers
from .models import Product

class ProducrSerializer(serializers.ModelSerializer):
#  my_discount = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = Product
    fields=[
      'title','content','price','sale_price','discount',
    ]

  
#    def get_my_discount(self,obj):
#        if not hasattr(obj,'id'):
#           return None
#        if not isinstance():
#           return None

#        return obj.discount()

