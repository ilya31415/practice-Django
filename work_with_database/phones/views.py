from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort')

    Phone_ = Phone.objects.all()
    context = {'phones': Phone_}
    if sort:
        list_name = [i for i in Phone_]
        if sort == 'name':
            list_name.sort(key=lambda x: x.name)
            context = {'phones': list_name}
            return render(request, template, context)
        elif sort == 'max_price':
            list_name.sort(key=lambda x: x.price, reverse=True)
            context = {'phones': list_name}
            return render(request, template, context)
        elif sort == 'min_price':
            list_name.sort(key=lambda x: x.price)
            context = {'phones': list_name}
            return render(request, template, context)

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    post = get_object_or_404(Phone, slug=slug)
    context = {'phone': post}
    return render(request, template, context)
