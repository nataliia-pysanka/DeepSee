from django.shortcuts import render
from .models import Product

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ProductSerializer, OrderProductSerializer


class ProductsListView(APIView):
    """Displaying all products in the store on JSON"""
    def get(self, request):
        queryset = Product.objects.all()
        if queryset:
            serializer_for_queryset = ProductSerializer(
                instance=queryset,
                many=True
            )
            return Response(serializer_for_queryset.data,
                            status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class CreateProductView(ProductsListView):
    """Create a new product in the store"""
    def post(self, request):
        serializer = ProductSerializer(
            data=request.data,
            many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class OrderProductView(ProductsListView):
    """Order a product in the store"""
    def put(self, request):
        try:
            product = Product.objects.get(name=request.data['name'])
        except Product.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT,
                          data=f"Product {request.data['name']} doesn't exist")
        if product:
            serializer = OrderProductSerializer(instance=product,
                                                data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


def product_list(request):
    """
    Controller for displaying a list of all records on the main page.
    :param request:
    :return: render
    """
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})
