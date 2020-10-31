from django.shortcuts import render
from products.models import Product
# Create your views here.


def all_cheese_products(request):
    """ View to render all products including sorting and searching """

    all_cheese_products = Product.objects.filter(category=1)

    context = {
        'products': all_cheese_products,
    }

    # context required to allow sending things back to template
    return render(request, 'buildbasket/cheese.html', context)
