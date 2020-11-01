from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from products.models import Product
from django.views.decorators.csrf import csrf_protect
from bag.views import view_bag, add_to_bag


@csrf_protect
def step1(request):
    cheeses = Product.objects.all().filter(category = 1)
    context = {
        'products': cheeses,
    }

    if request.method == 'POST':
        selections = request.POST.getlist('cheeses')

        for item in selections:
            request.session['builder_session'] += item

        return redirect('step2')
    return render(request, 'buildbasket/step1.html', context)


@csrf_protect
def step2(request):
    meats = Product.objects.all().filter(category=2)
    context = {
        'products': meats,
    }

    if request.method == 'POST':
        selections = request.POST.getlist('meats')
        if 'builder_session' in request.session:
            for item in selections:
                request.session['builder_session'] += item

        redirect('last_step')
    return render(request, 'buildbasket/step2.html', context)



@csrf_protect
def last_step(request):
    drinks = Product.objects.all().filter(category=4)

    context = {
        'products': drinks,
    }

    if request.method == 'POST':
        selections = request.POST.getlist('alcoholic_drinks')
        if 'builder_session' in request.session:
            for item in selections:
                request.session['builder_session'] += item

        print(request.session['builder_session'])
        return redirect(view_bag)
    return render(request, 'buildbasket/last_step.html', context)


# def step4(request):
#     if request.method == 'POST':
#         if form.is_valid():
#             pet = form.save(commit=False)
#             person = Person.objects.create(fn=request.session['fn'])
#             pet.owner = person
#             pet.save()
#             return HttpResponseRedirect(reverse('finished'))
#     return render(request, 'step1.html')
