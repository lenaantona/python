# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11
def input_num():
 correct = False
 while not correct:
    try:
        num = float(input('Введите вещественное число:\n'))
        correct = True
    except ValueError:
        print('Не является числом"\n')
 return num 

numbers = input_num()        
sum = 0
i = 1
if numbers < 0: i = -1
s = str(abs(numbers))
l = len(s) - s.find('.') - 1
num = abs(numbers * (100**l))

while num > 0:
    if 0< num< 10: sum = sum + (num % 10) * i
    else: sum = sum + num % 10
    num = (num - num % 10)/10
print(int(sum))
