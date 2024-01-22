from rest_framework import serializers

from django.contrib.auth.models import User

from store.models import Product,BasketItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class ProductSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields="__all__"
        

class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=BasketItem
        fields="__all__"
        read_only_fields=["id","basket","product","created_at","updated_at","is_active"]