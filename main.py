from pprint import pprint


def get_cook_book():
    cook_book = {}
    with open("recipes.txt", encoding="cp1251") as f:
        for line in f:
            key = line.strip()
            ingredient_list = []
            for i in range(int(f.readline().strip())):
                value = f.readline().strip()
                value_split = value.split(" | ")
                ingredient_dict = {'ingredient_name': value_split[0], 'quantity': value_split[1],
                                   'measure': value_split[2]}
                ingredient_list.append(ingredient_dict)
                cook_book[key] = ingredient_list
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingridient_dict = {}
    for key in dishes:
        if key in list(get_cook_book().keys()):
            ingridient_list = get_cook_book()[key]
            for ingridient in ingridient_list:
                if ingridient['ingredient_name'] in ingridient_dict.keys():
                    value = ingridient_dict[ingridient['ingredient_name']]
                    quantity = int(value['quantity']) + int(ingridient['quantity']) * person_count
                    ingridients = {ingridient['ingredient_name']: {'measure': ingridient['measure'],
                                                                   'quantity': quantity}}
                    ingridient_dict.update(ingridients)
                else:
                    ingridients = {ingridient['ingredient_name']: dict(measure=ingridient['measure'], quantity=int(
                        ingridient['quantity']) * person_count)}
                    ingridient_dict.update(ingridients)
    return ingridient_dict


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 4))
