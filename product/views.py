from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    top_products=Product.objects.all().order_by("-product_added")[:10]
    return render(request, 'product/index.html', {"top_products" : top_products})

def men_product_view(request):
    return render(request, 'product/men.html')