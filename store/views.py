from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.decorators import action

from store.serializers import UserSerializer,ProductSerializer,BasketItemSerializer
from store.models import Product

# Create your views here.

class SignUpView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class ProductsView(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    # url:http://127.0.0.1:8000/api/products/{id}/add_to_basket/
    
    @action(methods=["post"],detail=True)
    def add_to_basket(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product_object=Product.objects.get(id=id)
        basket_object=request.user.cart
        serializer=BasketItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product_object,basket=basket_object)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


    
    



