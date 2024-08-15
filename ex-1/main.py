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


if __name__ == "__main__":
    cook_book = {}
    file_list = read_file()

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