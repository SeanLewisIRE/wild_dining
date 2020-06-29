from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
# Create your views here.

def all_products(request):
    """ View to render all products including sorting and searching """
    products = Product.objects.all()
    query = None 
    categories = None
    """if statement is to allow searching of products. Search form action links to product view"""
    
    if request.GET: 
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET: 
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered", redirect(reverse('products')))
            queries = Q(name__icontains = query) | Q(description__contains = query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)  # context required to allow sending things back to template
    

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    # context required to allow sending things back to template
    return render(request, 'products/product_detail.html', context)
