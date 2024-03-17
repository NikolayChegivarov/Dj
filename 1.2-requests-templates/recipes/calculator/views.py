from django.shortcuts import render, Http404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def get_recipe(request, dish_name):
    if dish_name not in DATA:
        raise Http404("Рецепт не найден!")

    servings_number = int(request.GET.get('servings', 1))
    ingredients = DATA[dish_name].copy()  # Используем копию, чтобы не изменять исходный словарь
    for ingredient, value in ingredients.items():
        ingredients[ingredient] = servings_number * value

    context = {
        'recipe': ingredients
    }
    return render(request, 'calculator/index.html', context)