from django.shortcuts import render
from django.http import HttpResponse

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
    # можете добавить свои рецепты ;)
}

def calculate_ingridients(reqeust, dish):
    number_of_person = int(reqeust.GET.get('servings', 1))
    ingredients = {'recipe': DATA[dish]}
    for ingredient, value in ingredients['recipe'].items():
        ingredients['recipe'][ingredient] = value * number_of_person

    return render(reqeust, 'calculator/index.html', context=ingredients)

def get_dish_name(request):

    return HttpResponse(f'Внесите в путь название блюда из данного списка: {", ".join(DATA.keys())}.'
                        f' Пример /название блюда/?servings=количество персон')
