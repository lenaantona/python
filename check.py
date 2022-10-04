global str_err
str_err = ''

def check_number(num1, num2, r):
    num = []
    try:
        if r == 2:
            num1 = float(num1)
            num2 = float(num2)
        elif r == 1:
            num1 = complex(num1)
            num2 = complex(num2)
    except ValueError:
        if r == 2:
            str_err = 'Неверно ввели одно из рациональных чисел. Повторите ввод'
        elif r == 1:
            str_err = 'Неверно ввели одно из комплексных чисел. Повторите ввод'
        return str_err
    num.append(num1)
    num.append(num2)
    return num

def check_regime(num):
    if num == '1':
        return 1
    elif num == '2':
        return 2
    else:
        return "Неверно ввели режим калькулятора (1, 2)"

