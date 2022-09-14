# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
numbers= int(input('Введите целое число '))
str_list = ''
def fun(num):
  '''
  функция переводит десятичное число в двоичное
  '''
  global str_list
  if num == 1:
    str_list = '{}{}'.format(1,str_list)
  else:
    str_list = '{}{}'.format(num%2,str_list)
    fun(int(num/2))

fun(numbers)
print(str_list)