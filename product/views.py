from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Product, Category

# Create your views here.

def index(request):
    top_products=Product.objects.all().order_by("-product_added")[:10]
    return render(request, 'product/index.html', {"top_products" : top_products})

def men_product_view(request):
    try:
        men_products=Product.objects.filter(product_category=Category.objects.filter(category_name="men").first())
    except Category.DoesNotExist:
        men_products=Category.objects.none()
    return render(request, 'product/men.html', {"products" : men_products})


def women_product_view(request):
    try:
        women_products=Category.objects.get(category_name="women").products.all()
    except Category.DoesNotExist:
        women_products=Category.objects.none()

    return render(request, 'product/women.html', {"products" : women_products})


def kids_product_view(request): 
    return render(request, 'product/kids.html')
