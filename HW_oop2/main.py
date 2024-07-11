import re


def get_ingredients_from_file(file_name: str):
    ingredient_list = []
    dish_names = []
    ingredient_counts = []
    print(f'Openning file {file_name}')
    with open(file_name, encoding='utf-8') as book:
        for line in book:
            if '|' not in line and not re.match(r'^[0-9]+$', line) and line != '\n':
                dish_names.append(line.strip())
            elif re.match(r'^[0-9]+$', line) and '|' not in line:
                ingredient_counts.append(line.strip())
            elif line != '\n':
                changed_line = [splited_line.strip() for splited_line in line.split('|')]
                ingredient_list.append(changed_line)

    return ingredient_list, dish_names, ingredient_counts


def create_cook_book_dict(file_name: str):
    ingredients, dishes, ingredients_num = get_ingredients_from_file(file_name)
    cook_book = {}
    dish_shfit = 0
    for dish_name, count in zip(dishes, ingredients_num):
        cook_book[dish_name] = []
        for ingredient in ingredients[dish_shfit: dish_shfit + int(count)]:
            cook_book[dish_name].append({'ingredient_name': ingredient[0], 'quantity': ingredient[1],
                                         'measure': ingredient[2]})
        dish_shfit += int(count)

    return cook_book

def get_shop_list_by_dishes(dishes: list, person_count: int):
    cook_book = create_cook_book_dict('task1.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    ingredient_count = (shop_list[ingredient['ingredient_name']]['quantity']
                                        + int(ingredient['quantity']) * person_count)
                else:
                    ingredient_count = int(ingredient['quantity']) * person_count
                shop_list.setdefault(ingredient['ingredient_name'], ingredient)
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': ingredient_count}
    return shop_list

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
