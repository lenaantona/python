# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

def numbers(new_list):
    n = 1
    l = len(new_list)
    for i in new_list:
        for j in range(n, l):
            if i == new_list[j]:
                new_list[j] = ''
        n += 1    
    new_list = list(filter(None, new_list))
    return new_list

input_list = [1, 1, 7, 3, 5, 3, 7, 8, 9, 9]
print(numbers(input_list))


