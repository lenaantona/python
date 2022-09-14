# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1999, 8.2444, 6.98] - 0.91 или 91

list = [4.07, 5.19999, 8.2444, 6.98]

def fractional_list(input_list):
  '''
  функция создает новый спиок только дробной части числа
  '''
  new_list = []
  for i in list:
    s = str(i)
    count = abs(s.find('.') - len(s)) - 1
    new_list.append(round(i-int(i),count))
  return new_list

def result_max_min(input_list):
  '''
  функция возращает разницу максимального и минимального элемента списка
  '''
  min = input_list[0]
  max = input_list[0]
  for i in input_list:
      if i > max: max = i
      if i < min: min = i
  s_max = str(max)
  s_min = str(min)
  count_max = abs(s_max.find('.') - len(s_max)) - 1
  count_min = abs(s_min.find('.') - len(s_min)) - 1
  if count_max > count_min: count = count_max
  else: count = count_min
  return(round((max-min),count))

print(fractional_list(list))
print(result_max_min(fractional_list(list)))


    