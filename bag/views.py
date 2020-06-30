from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ View to render shopping bag """
    return render(request, 'bag/bag.html')
