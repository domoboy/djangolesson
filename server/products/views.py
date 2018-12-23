from django.shortcuts import render
import json
from .models import CategoryProduct, Product


def list_view(request):
    return render(request, 'products/list.html', {'products': Product.objects.all()})


def detail_view(request, pk):
    return render(request, 'products/detail.html', {'object': Product.objects.get(id=pk)})
