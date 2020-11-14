from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from products.models import Product
from django.views.decorators.csrf import csrf_protect
# from .forms import cheesesSelection1
# from bag.views import view_bag, add_to_bag


@csrf_protect
def step1(request):

    if request.method == 'POST':
        form = cheesesSelection1(request.POST)
        if form.is_valid():
            selections = request.POST.getlist('cheeses')
            return render(request, 'buildbasket/step1.html', context)
        
    # cheeses = Product.objects.all().filter(category = 1)
    # context = {
    #     'products': cheeses,
    # }

    # if request.method == 'POST':
    #     selections = request.POST.getlist('cheeses')
    #     print(selections)
    #     request.session['builder_session'] = selections

    # print(request.session['builder_session'])
    # return render(request, 'buildbasket/step1.html', context)


@csrf_protect
def step2(request):
    meats = Product.objects.all().filter(category=2)
    context = {
        'products': meats,
    }

    if request.method == 'POST':
        selections = request.POST.getlist('meats')
        request.session['builder_session'] = selections
    
    return redirect('step3')
    print(request.session['builder_session'])
    return render(request, 'buildbasket/step2.html', context)



@csrf_protect
def step3(request):
    drinks = Product.objects.all().filter(category=4)

    context = {
        'products': drinks,
    }

    if request.method == 'POST':
        selections = request.POST.getlist('alcoholic_drinks')
        request.session['builder_session'] = selections

    return redirect('done')
    print(request.session['builder_session'])
    return render(request, 'buildbasket/step3.html', context)


def done(request):
    built_basket = request.session['builder_session']
    print(built_basket)
    context = {
        'selection': built_basket,
    }

    return render(request, 'buildbasket/done.html', context)


# def step4(request):
#     if request.method == 'POST':
#         if form.is_valid():
#             pet = form.save(commit=False)
#             person = Person.objects.create(fn=request.session['fn'])
#             pet.owner = person
#             pet.save()
#             return HttpResponseRedirect(reverse('finished'))
#     return render(request, 'step1.html')
