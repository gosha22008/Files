# Задача №3
import os
path = os.getcwd()

def get_txt_files(path):
    all_files = os.listdir(path)
    txt_files = filter(lambda x: x.endswith('.txt'), all_files)
    return txt_files

def fun_name(txt_list):
    my_dict_data = {}
    my_dict_len = {}
    for txt_file in txt_list:
        my_new_list = []
        with open(txt_file, 'r', encoding='utf-8') as file:
            for line in file:
                my_str = line.strip()
                my_new_list.append(my_str)
            my_dict_len[txt_file] = len(my_new_list)
            my_dict_data[txt_file] = my_new_list
    return [my_dict_data, my_dict_len]

def sort_fun(list):
    sorted_tuple = sorted(list[1].items(), key=lambda x: x[1])
    return [sorted_tuple, list[0]]

def write_fun(list):
    with open('Result.txt', 'a', encoding='utf-8') as file:
        n = 0
        for tuple in list[0]:
            if n == 0:
                file.write(f'''{tuple[0]}\n{tuple[1]}\n''')
            else:
                file.write(f'''\n{tuple[0]}\n{tuple[1]}\n''')
            n += 1
            for string in list[1][tuple[0]]:
                file.write(string+'\n')
write_fun(sort_fun(fun_name(get_txt_files(path))))