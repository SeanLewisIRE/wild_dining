from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_bag(request):
    """ View to render shopping bag """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """Add a user specified quantity of an item to the bag"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust a user specified quantity of an item to the bag"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove an item from the bag"""
    bag = request.session.get('bag', {})
    bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
