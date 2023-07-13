import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse,HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from prod.models import Product
from prod.serializers import ProductSerializer


@api_view(["GET"])
def get_home(request, *args, **kwargs):
    products = Product.objects.all()
    product_list = [model_to_dict(product) for product in products]
    return Response(product_list)


@api_view(["POST"])
def post_home(request, *args, **kwargs):
    """DRF API VIEWS"""
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        isinstance = serializer.save()
        print(isinstance)
        return Response(serializer.data)
    return Response({"invalid" : "not good data"}, status=400)