import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    testdict = {}
    path = ''
    result = []

    for dirpath, dirnames, filenames in os.walk(""):
        for dirname in dirnames:
            testdict[os.path.join(dirpath, dirname)] = []

        for filename in filenames:
            for i in testdict:
                if i in os.path.join(dirpath, filename):
                    testdict[i].append(f'Файл: {filename}')

        result = [f'<p style = "color:red">Каталог {key}: </p> {values}' for key, values in testdict.items()]

    return HttpResponse('<p> </p>'.join(result))
