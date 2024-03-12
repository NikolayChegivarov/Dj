from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.utils import formats
import datetime
import os
from django.http import JsonResponse


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
        'Текст': reverse('index')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def index_view(request):
    return HttpResponse('Happened.')


def time_view(request):
    current_datetime = datetime.datetime.now()
    formatted_datetime = formats.date_format(current_datetime, "SHORT_DATETIME_FORMAT")
    msg = f'Текущее время: {formatted_datetime}'
    return HttpResponse(msg)


def workdir_view(request):
    # Получаем список файлов в текущей рабочей директории
    files = os.listdir('.')
    # Возвращаем список файлов в формате JSON
    return JsonResponse({'files': files})
