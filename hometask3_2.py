# #2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


def composition_numbers(input_list):
    '''
  функция возращает произведение пар чисел списка, первого и последнего, второго и предпоследнего и тд
  '''
    l = len(input_list)
    list_result = []
    j = 0
    for i in range(0, int(l / 2)):
        list_result.append(input_list[i] * input_list[l - 1 - j])
        j += 1
    if l % 2 != 0:
        list_result.append(input_list[(int(l / 2))]**2)
    return (list_result)


list_numbers = [2, 3, 4, 5, 6]
print(composition_numbers(list_numbers))
