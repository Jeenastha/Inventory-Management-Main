from rest_framework.serializers import ModelSerializer
from .models import Product,ProductType

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'          #['name']

class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model=ProductType
        fields='__all__'        