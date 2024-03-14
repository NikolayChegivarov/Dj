from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.utils import formats
import datetime
import os
from django.http import JsonResponse

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

def home_dishes(request):

    template_name = 'calculator/index.html'

    pages = {
        'Рецепты': reverse('home'),
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def omlet_view(request):
    omlet_ingredients = DATA['omlet']
    return HttpResponse(f'Ингридиенты для омлета: {omlet_ingredients}')

    # context = {
    #   'recipe': {
    #     'ингредиент1': количество1,
    #     'ингредиент2': количество2,
    #   }
    # }
    # return render(request, template_name, context)

def pasta_view(request):
    pasta_ingredients = DATA['pasta']
    return HttpResponse(f'Ингридиенты для омлета: {pasta_ingredients}')

def buter_view(request):
    buter_ingredients = DATA['buter']
    return HttpResponse(f'Ингридиенты для омлета: {buter_ingredients}')

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
