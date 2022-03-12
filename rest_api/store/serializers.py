from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    amount_in_stock = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(self)
        instance.name = validated_data.get('name', instance.name)
        instance.amount_in_stock += validated_data.get('amount_in_stock',
                                                      instance.amount_in_stock)
        instance.save()
        return instance


class OrderProductSerializer(ProductSerializer):
    def update(self, instance, validated_data):
        print(self)
        instance.name = validated_data.get('name', instance.name)
        amount = validated_data.get('amount_in_stock',
                                    instance.amount_in_stock)
        if instance.amount_in_stock > amount:
            instance.amount_in_stock -= amount
        else:
            instance.amount_in_stock = 0
        instance.save()
        return instance
