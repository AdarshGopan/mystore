from rest_framework import serializers
from api.models import Products,Reviews,Carts

class ProductSerializer(serializers.Serializer):
    name=serializers.CharField()
    description=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    image=serializers.ImageField()
    
class ProductModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Products
        fields=["name","description","category","price","image"]

class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    
    class Meta:
        model=Reviews
        fields=["comment","rating","user","product"]
        
    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")

        return Reviews.objects.create(**validated_data,user=user,product=product)

class CartSerializer(serializers.ModelSerializer):
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)

    class Meta:
        model=Carts
        fields=["product","user","date"]

    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")

        return Carts.objects.create(**validated_data,user=user,product=product)