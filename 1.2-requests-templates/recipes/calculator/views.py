from django.shortcuts import render, reverse

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

def home_view(request):

    template_name = 'calculator/index.html'

    recipe = {
        'Рецепты': reverse('home'),
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }

    context = {
        'recipe': recipe
    }
    return render(request, template_name, context)


def get_ingredients(dish, servings=1):
    ingredients = DATA.get(dish, {})
    return {ingredient: quantity * servings for ingredient, quantity in ingredients.items()}

def omlet_view(request):
    servings = request.GET.get('servings', 1)
    servings = int(servings)
    ingredients = get_ingredients('omlet', servings)
    context = {'recipe': ingredients}
    return render(request, 'calculator/index.html', context)

def pasta_view(request):
    servings = request.GET.get('servings', 1)
    servings = int(servings)
    ingredients = get_ingredients('pasta', servings)
    context = {'recipe': ingredients}
    return render(request, 'calculator/index.html', context)

def buter_view(request):
    servings = request.GET.get('servings', 1)
    servings = int(servings)
    ingredients = get_ingredients('buter', servings)
    context = {'recipe': ingredients}
    return render(request, 'calculator/index.html', context)