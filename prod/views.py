from rest_framework import generics

from .models import *
from .serializers import *

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def preform_create(self, serizlizer):
        title = serizlizer.validated_data.get('title')
        content = serizlizer.validated_data.get('content')
        if content is None:
            content = title
        serizlizer.save(content = content)

product_detail_view = ProductDetailAPIView.as_view()

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()