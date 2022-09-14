# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def sum_oddnumbers(input_list):
  '''
  Функция возращает сумму элементов списка на нечетных позициях
  '''
  sum = 0
  l = len(input_list)
  for i in range(0, l-1):
   if (i%2 != 0):
      sum = sum + input_list[i]
  return sum
  
numbers = [2, 3, 5, 9, 3]
result = sum_oddnumbers(numbers)
print(result)