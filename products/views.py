from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def all_products(request):
    """ View to render all products including sorting and searching """
    products = Product.objects.all()

    context = {
        'products':products,
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
