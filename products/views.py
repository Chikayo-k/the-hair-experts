from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ItemForm


# Create your views here.

def all_products(request):
    """
    View to show all products
    sorting and search queries
    """

    products = Product.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        """
        Sorting
        """
        if 'sort' in request.GET:
            sortkeyword = request.GET['sort']
            sort = sortkeyword 
            if sortkeyword == 'name':
               sortkeyword = 'lower_name'
               products = products.annotate(lower_name=Lower('name'))
            if sortkeyword == 'category':
                sortkeyword='category__name'            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkeyword  = f'-{sortkeyword }'
            products = products.order_by(sortkeyword )

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
                messages.error(request,'No search criteria was enterd !')
                return redirect(reverse('products'))
            
            queries = Q(name__icontains = query) | Q(description__icontains=query)
            products = products.filter(queries)
    
    sorting = f'{sort}_{direction}'


    context = {
        'products': products,
        'search_word':query,
        'cureent_categories':categories,
        'sorting':sorting,
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

    
def add_item(request):
    """
    Add items (admin)
    """
    if request.method =='POST':
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Item was added successfully!')
            return redirect(reverse('detail',args=[item.id]))
        else:
            messages.error(request, 'Failed. Please try again!')
    else:
        form = ItemForm()
    template ='products/add_item.html'
    context ={
        'form':form,
    }

    return render(request,template,context)


def edit_item(request, product_id):
    """
    Edit item in stock
    """
    item = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form= ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated stock successfully!')
            return redirect(reverse('detail',args=[item.id]))
        else:
            messages.error(request,'Failed to update stock. Please try again.')
    else:
        form = ItemForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template ='products/edit_item.html'
    context ={
        'form':form,
        'item':item,
    }

    return render(request,template,context)

def delete_item(request, product_id):
    """
    Delete item from stock
    """
    item = get_object_or_404(Product, pk=product_id)
    item.delete()
    messages.success(request,'Item has been deleted!')
    return redirect(reverse ('products'))

    





