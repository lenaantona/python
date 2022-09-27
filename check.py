import view
import logger as l

def check_realnumber():
    correct = False
    while not correct:
        try:
            num = float(view.get_value())
            correct = True
        except ValueError:
            print('Неверно ввели реляционное число')
            l.input_error('Неверно ввели реляционное число')
    return num

def check_complexnumber():
    correct = False
    while not correct:
        try:
            num = complex(view.get_value())
            correct = True
        except ValueError:
            print('Неверно ввели комлексное число')
            l.input_error('Неверно ввели комлексное число')
    return num

def check_regime():
    correct = False
    while not correct:
        try:
            num = int(view.get_regime())
            if num in [0, 1, 2]:
                correct = True
        except ValueError:
            print("Неверно ввели режим калькулятора (0, 1, 2")
            l.input_error('Неверно ввели режим калькулятора')
    return num

def check_operation():
    oper_list = ['+', '-', '*', '/']
    correct = False
    while not correct:
        oper = view.get_operations()
        if oper in oper_list:
            correct = True
            return oper
        else:
            print('Неверно введена операция (+,-,/,*)')
            l.input_error('Неверно введена операция')