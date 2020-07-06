from django.shortcuts import render, get_object_or_404
from .models import Categories, Products


def index(request):
    return render(request, 'meb/index.html')


def shop(request, slug_category=None):
    category = Categories.objects.all()
    product = Products.objects.all()

    price_from = request.GET.get("min", "")
    price_to = request.GET.get("max", "")

    if price_from == '':
        price_from = '0'
        price_to = '500000'
    else:
        product = Products.objects.filter(price__gte=int(price_from), price__lte=int(price_to))

    if slug_category:
        category = Categories.objects.all()
        selected_category = get_object_or_404(Categories, slug_category=slug_category)
        product = Products.objects.filter(category=selected_category)

        price_from = request.GET.get("min", "")
        price_to = request.GET.get("max", "")

        if price_from == '':
            price_from = '0'
            price_to = '500000'
        else:
            product = Products.objects.filter(category=selected_category, price__gte=int(price_from), price__lte=int(price_to))

    context = {
        'price_from': price_from,
        'price_to': price_to,
        'category': category,
        'product': product,
    }

    return render(request, 'meb/shop.html', context)


def design(request):
    return render(request, 'meb/ideas.html')


def about(request):
    return render(request, 'meb/about.html')


def contact(request):
    return render(request, 'meb/contact.html')