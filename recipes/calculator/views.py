from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home(request):
    k = [i for i in range(2, 21)]
    dish = request.GET.get('dish', 'home')
    context = {
        'qwe': k,
        'dish': dish
    }
    return render(request, 'calculator/home.html', context)


def omlet(request, servings):
    recipe = {}
    for k, v in DATA['omlet'].items():
        recipe[k] = v * servings

    context = {
        'recipe': recipe,
    }

    return render(request, 'calculator/index.html', context)


def pasta(request, servings):
    recipe = {}
    for k, v in DATA['pasta'].items():
        recipe[k] = v * servings

    context = {
        'recipe': recipe,
    }

    return render(request, 'calculator/pasta.html', context)


def buter(request, servings):
    recipe = {}
    for k, v in DATA['buter'].items():
        recipe[k] = v * servings

    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/buter.html', context)


def dish_1(request):
    dish = request.GET.get('dish', 'home')
    print(request.GET)
    servings = int(request.GET.get('servings', 1))

    return redirect(reverse(dish, kwargs={'servings': servings}))
