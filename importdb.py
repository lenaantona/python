# 1) функция считывает внешний файл !!!JSON!!!распарсила его и собрала в список списков file_json_read_for_import(file) return list list1 = [[di1,imya1,fam2], [di2,imya2,fam], [di3,imya3,fam]] нужен ли /n d?
# !!!!!! каждый элемент списка с новой строки 
# 2) функция которая записывает каждый элемент списка полученного от file_read_for_import() с помощью db_input() в цикле db_import(list)
# for i in file_read_for_import():
#     db_input()

# 3) функция считывает внешний файл !!!CVS!!!распарсила его и собрала в список списков file_CVS_read_for_import(file) return list list1 = [[di1,imya1,fam2], [di2,imya2,fam], [di3,imya3,fam]] нужен ли /n d?
# !!!!!! каждый элемент списка с новой строки 

import json
import csv
import operations as oper
from os.path import exists

def json_parse(filename: str) -> list[dict[str, str]]:
    with open(filename, 'r', encoding='utf-8') as read_file:
        data = json.load(read_file)
    return data

def import_to_csv(data, filename):
    list_data = oper.convert_dics_to_list(data)
    if any(len(row) != len(oper.header) for row in list_data):
        raise Exception
    is_existed = exists(filename)
    with open(filename, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        if is_existed:
            #writer.writerows(list_data)
            for row in list_data:
                oper.db_input(row[1:])
        else:
            writer.writerows([oper.header, *list_data])
       
def db_import(filename_json, filename_csv):
    data = json_parse(filename_json)
    import_to_csv(data, filename_csv)


