#Задачи 1 и 2
from pprint import pprint

def get_data():
    cook_book = dict()
    with open('file_recepts', 'r', encoding='utf-8') as file:
        for line in file:
            name = line.strip()
            igredient_quantity = int(file.readline().strip())
            my_list = []
            for n in range(igredient_quantity):
                structure = file.readline().strip().split('|')
                my_list.append({'ingredient_name': structure[0], 'quantity': structure[1], 'measure': structure[2]})
            file.readline()
            cook_book[name] = my_list
    return cook_book
pprint(get_data())
print('==='*30)

def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    my_dict = {}
    cook_book = get_data()
    keys_list = cook_book.keys()
    for dish in dishes:
        if dish in keys_list:
            for dict in cook_book[dish]:
                my_values = dict['ingredient_name']
                del(dict['ingredient_name'])
                if my_values in my_dict.keys():
                    dict['quantity'] = int(dict['quantity']) * person_count*2
                else:
                    dict['quantity'] = int(dict['quantity']) * person_count
                my_dict[my_values] = dict
        else:
            print(f'{dish} такого блюда в списке нет!')
    return my_dict
pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))
