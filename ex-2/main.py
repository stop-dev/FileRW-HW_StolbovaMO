import os
from pprint import pprint


def read_file() -> list:
    with open(os.path.join(os.getcwd(), 'files/src.txt')) as f:
        file_list = f.readlines()
    return [s.strip() for s in file_list]


def ingredients_list(ingredients_list: list) -> list:
    KEYS = ['ingredient_name', 'quantity', 'measure']
    res = []

    for ingredient in ingredients_list:
        values = ingredient.split(" | ")
        values[1] = int(values[1])
        res.append(dict(zip(KEYS, values)))
    return res


def cook_book_init(file_list: list) -> dict:
    cook_book = {}

    if not len(file_list):
        dish_index_list = []
        print("Empty file")
    else:
        dish_index_list = [0] + [id_ + 1 for id_, s in
                                  enumerate(file_list) if not len(s)]
    for dish_id in dish_index_list:
        ingredient_id = dish_id + 2
        ingredient_num = int(file_list[dish_id + 1])
        recipe_list = file_list[ingredient_id:ingredient_id + ingredient_num]
        cook_book[file_list[dish_id]] = ingredients_list(recipe_list)
    return cook_book

    
    
def get_shop_list_by_dishes(dishes: list, person_count: int,
                             cook_book:dict) -> dict:
    ERROR1 = "No {}'s recipe(s) in cook_book."
    ERROR2 = "person_count less then one. You don't need to cook."
    recipe_valid = set(dishes).difference(set(cook_book))
    shop_list = {}

    if (recipe_valid):
        print(ERROR1.format('\'s, '.join(dishes)))
        return shop_list
    if (person_count < 1):
        print(ERROR2)
        return shop_list
    for dish in dishes:
        for ingredient_info in cook_book[dish]:
            ingredient = ingredient_info['ingredient_name']
            if not ingredient in shop_list:
                shop_list[ingredient] = {'measure':ingredient_info['measure']}
                shop_list[ingredient]['quantity'] = (ingredient_info['quantity']
                                                     * person_count)
            else:
                shop_list[ingredient]['quantity'] += (ingredient_info['quantity']
                                                      * person_count)
    return shop_list


if __name__ == "__main__":
    file_list = read_file()
    cook_book = cook_book_init(file_list)

    # В файл src.txt в 'Запеченный картофель' добавлен повторяющийся
    #  ингридиент 'Помидор'
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book))


