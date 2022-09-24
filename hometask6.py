from functools import reduce
import random

# 1- Определить, присутствует ли в заданном списке строк, некоторое число

# str_list = ['nnvhh', '12', 'nvjv', 'fgfh2']

# def search_str(str1):
#     res = list(filter(lambda i: i.isdigit(), str1))
#     return (res)

# result_list = list(filter(search_str, str_list))
# print(result_list)


# 2 - Найти сумму чисел списка стоящих на нечетной позиции

# new_list = [random.randint(0, 10) for i in range(8)]
# print(f'Исходный массив {new_list}')
# result_list = reduce(lambda i, j: i+j, new_list[1::2])
# print(f'Сумма на нечентых позициях {result_list}')



# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

# def distance(x,y):
#     return (sum(map(lambda x1,y1 : (int(x1)-int(y1))**2,x,y)))**0.5
    
# x_list = input('Введите координаты точки X через пробел: ').split(' ')
# y_list = input('Введите координаты точки Y через пробел: ').split(' ')

# # print(distance(x_list,y_list))



# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# new_list = ["qwe", "asd", "zxc", "qwe", "rtqwe"]
# next_list = list(enumerate(new_list))

# def search2(input_list):
#     if 'qwe' in input_list[1]:
#         return True
#     else: False

# result_list = list(filter(search2, next_list))
# print(result_list[1][0])


# 5- Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# def omposition_numbers(x, y):
#     return list(map(lambda x1,y1 : x1+y1, x,y))

# new_list = [random.randint(0, 10) for i in range(8)]
# print(f'Исходный массив {new_list}')
# l = len(new_list)
# if l%2 == 0:
#     print(omposition_numbers(new_list[:int(l/2)], new_list[:int(l/2-1):-1]))
# else: 
#     print(omposition_numbers(new_list[:int(l/2)+1], new_list[:int(l/2-1):-1]))



# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
# def input_num():
#     correct = False
#     while not correct:
#         try:
#             num = int(input('Введите целое число:\n'))
#             correct = True
#         except ValueError:
#                 print('Не является числом"\n')
#     return num   
# num = input_num()
# result_list = [((-3)**i) for i in range(0, num)]
# print(result_list)