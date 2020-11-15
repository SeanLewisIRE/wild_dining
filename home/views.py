from django.shortcuts import render
from products.models import Category


# Create your views here.
def index(request):

    # del request.session['bag']

    categories = Category.objects.all()
    context = {
        'categories': categories,
    }

    """ View to render index.html """
    return render(request, 'home/index.html', context)
