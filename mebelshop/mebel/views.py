from django.shortcuts import render
from .models import Categories, Products


def index(request):
    return render(request, 'meb/index.html')


def shop(request):
    category = Categories.objects.all()
    product = Products.objects.all()

    context = {
        'category': category,
        'product': product,
    }

    return render(request, 'meb/shop.html', context)