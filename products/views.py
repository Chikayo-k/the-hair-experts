from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
    """
    View to show all products
    sorting and search queries
    """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                message.error(request,'Try again!')
                return redirect(reverse('products'))
            
            queries = Q(name__icontains = query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
        'search_word':query,
    }

    return render(request, 'products/products.html', context)

def detail(request, product_id):
    """
    View to show details of product
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/detail.html', context)

