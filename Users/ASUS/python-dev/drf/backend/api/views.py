from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProducrSerializer
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProducrSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"Not valid"},status=400)