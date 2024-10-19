from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product,ProductType
from .serializers import ProductSerializer,ProductTypeSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# Create your views here.
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
 
class ProductTypeApiView(GenericAPIView): 
    queryset=ProductType.objects.all()
    serializer_class=ProductTypeSerializer
    
    def get(self,request):
        queryset=self.get_queryset()
        serializer=self.serializer_class(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data created')
        else:
            return Response(serializer.errors)
        
class ProductTypeApiDetailView(GenericAPIView):
    queryset=ProductType.objects.all()
    serializer_class=ProductTypeSerializer

    def get(self,request,pk):
        queryset=self.get_object()
        serializer=self.serializer_class(queryset)
        return Response(serializer.data)
    
    def put(self,request,pk):
        queryset=self.get_object()
        serializer=self.serializer_class(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data updated!')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        queryset=self.get_object()
        queryset.delete()
        return Response('data deleted')


            

    
  