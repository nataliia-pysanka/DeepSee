from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    amount_in_stock = serializers.IntegerField()

    def create(self, validated_data):
        instance, created = Product.objects.update_or_create(
            name=validated_data.get('name', None),
            defaults=validated_data)
        if not created:
            amount = validated_data.get('amount_in_stock',
                                        instance.amount_in_stock)
            instance.amount_in_stock += amount
            instance.save()
        return instance


class OrderProductSerializer(ProductSerializer):
    def update(self, instance, validated_data):
        # instance.name = Product.objects.get('name', instance.name)
        amount = validated_data.get('amount_in_stock',
                                    instance.amount_in_stock)
        instance.amount_in_stock -= amount
        instance.save()
        return instance

