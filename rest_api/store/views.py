from django.shortcuts import render
from .models import Product
from django import forms
import json


class JSONForm(forms.Form):
    JSON = forms.CharField(widget=forms.Textarea(attrs={'id': 'JSON'}))


def read_json(json_str):
    data = json.loads(json_str)
    for line in data:
        try:
            product = Product.objects.get(name=line['name'])
            product.amount_in_stock += line['amount']
            product.save()
        except Product.DoesNotExist:
            product = Product()
            product.name = line['name']
            product.amount_in_stock = line['amount']
            product.save()
    return


def product_list(request):
    if request.method == "POST":
        form = JSONForm(request.POST)
        if form.is_valid():
            json_str = f'{form.cleaned_data["JSON"]}'
            read_json(json_str)
            return render(request, 'store/product_list.html',
                          {'products': Product.objects.all()})
        else:
            return render(request, 'store/product_list.html',
                          {'products': Product.objects.all(), 'form': form})
    return render(request, 'store/product_list.html',
                  {'products': Product.objects.all(), 'form': JSONForm()})
