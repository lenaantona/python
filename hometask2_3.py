# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, 
# но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.
def input_num():
    correct = False
    while not correct:
        try:
            num = int(input('Введите вещественное число:\n'))
            correct = True
        except ValueError:
                print('Не является числом"\n')
    return num   

int_num = input_num()
num = list(str(int_num))

def polindrom(num1):
 l = len(num1)//2
 pol = 0
 for i in range(0, l):
    if num1[i]!=num1[-1-i]: pol = pol + 1
 return pol   

def new_polindrom(num2):
    int_num2 = 0
    num2.reverse()
    l = len(num2)
    for i in num2:
        l = l - 1
        int_num2 = int_num2 + int(i) * (10 ** l)
    return int_num2

p = polindrom(num)
if p == 0: print('Введенное число является полиндромом')
while p!=0:
    new_numbers = new_polindrom(num)
    new_numbers = new_numbers + int_num
    num = list(str(new_numbers))
    p = polindrom(num)

print('Для введенного числа полиндромом явлется {}'.format(new_numbers))

