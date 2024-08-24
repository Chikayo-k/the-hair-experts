from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """
    View to show all products
    sorting and search queries
    """

    products = Product.objects.all()

    query = None
    categories = None


    if request.GET:
        """
        Filter by category    
        """
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        """
        Search by keyword   
        """
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
        'cureent_categories':categories,
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

