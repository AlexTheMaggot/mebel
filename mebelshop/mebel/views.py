from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm
from .models import Categories, Products


def index(request):
    return render(request, 'meb/index.html')


def shop(request, slug_category=None):
    category = Categories.objects.all()
    product = Products.objects.all().order_by('-id')

    price_from = request.GET.get("min", "")
    price_to = request.GET.get("max", "")

    if price_from == '':
        price_from = '0'
        price_to = '500000'
    else:
        product = Products.objects.filter(price__gte=int(price_from), price__lte=int(price_to)).order_by('-id')

    selected_category = ''

    if slug_category:
        category = Categories.objects.all()
        selected_category = get_object_or_404(Categories, slug_category=slug_category)
        product = Products.objects.filter(category=selected_category).order_by('-id')

        price_from = request.GET.get("min", "")
        price_to = request.GET.get("max", "")

        if price_from == '':
            price_from = '0'
            price_to = '500000'
        else:
            product = Products.objects.filter(category=selected_category, price__gte=int(price_from), price__lte=int(price_to)).order_by('-id')


    paginator = Paginator(product, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    cart_product_form = CartAddProductForm()

    context = {
        'price_from': price_from,
        'price_to': price_to,
        'category': category,
        'product': product,
        'page_obj': page_obj,
        'selected_category': selected_category,
        'cart_product_form': cart_product_form,
    }

    return render(request, 'meb/shop.html', context)


def design(request):
    return render(request, 'meb/ideas.html')


def about(request):
    return render(request, 'meb/about.html')


def contact(request):
    return render(request, 'meb/contact.html')
