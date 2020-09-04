from django.shortcuts import render

from shop.models import Category, Product


def prodeuct_in_category(request) :
    categories = Category.object.all()
    products = Product.object.all()

    return render(request, 'shop/list.html', {'categories': categories, 'prodects': products})
