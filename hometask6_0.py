# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,. приоритет операций стандартный.
# Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 10/2*5 => 25;
# 10 * 5 * => недостаточно числовых данных
# -5 + 5 => 0
# два + три => неправильный ввод: нужны числа
# (2+((5-3)*(16-14)))/3 => 2
# # (256 - 194 => некорректная запись скобок


def transf_list(): # преобразование строки в список
    input_expres = input('Введите арифметическое выражение: ')
    input_expres = input_expres.replace(' ', '')
    global oper
    oper = {
        '*': lambda x, y: x*y,
        '/': lambda x,y: x/y,
        '+': lambda x,y: x+y,
        '-': lambda x,y: x-y
    }
    global znak
    znak = 1
    if input_expres[0] == '-':
        input_expres = input_expres[1:]
        znak = -1

    for i in oper:
       input_expres = input_expres.replace(i, f'${i}$')

    expres_list = input_expres.split('$')
    return expres_list

def exam_expres(): # проверка на корректоность преобразованного списка
    correct = False
    while not correct:
        try:
            expres_list = transf_list()
            expres1 = list(filter(lambda i: int(i), expres_list[0::2]))
            expres_list[0] = int(expres_list[0]) * znak
            expres2 = list(filter(lambda i: i in ['*', '/','+','-'],expres_list[1::2]))
            correct = True
        except ValueError:
                print('Введено неверно арифметическое выражение"\n')
    return expres_list  


def do_express(a,b, expres_list): # выполняется расчет арифметического выражения
    while (a in expres_list or b in expres_list):
        for i in range(len(expres_list)):
            if (expres_list[i]== a or expres_list[i]== b):
                expres_list[i] = oper.get(expres_list[i])(int(expres_list[i-1]),int(expres_list[i+1]))
                del expres_list[i-1]
                del expres_list[i]
                break
    return expres_list


result_list = exam_expres()
result_list = do_express('*', '/', result_list)
result_list = do_express('+', '-', result_list)
print(result_list)