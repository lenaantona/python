import  arithmetic_operations as oper
import view
import check as ch
import logger as l

def button_click():
    regim = ch.check_regime()  # режим (1- реляционные, 2 комплексные числа)
    if regim == 1:
        value_a = ch.check_realnumber()
        value_b = ch.check_realnumber()
    elif regim == 2:
        value_a = ch.check_complexnumber()
        value_b = ch.check_complexnumber()
    elif regim == 0:
        print('Программа завершена')
        l.exit_prog() # запись о закрытии программы
        exit()
    operator = ch.check_operation() # арифметическая операция (+,-,/,*)
    if operator == '+':
        result = oper.sum_oper(value_a,value_b)
    elif operator == '-':
        result = oper.sub_oper(value_a,value_b)
    elif operator == '*':
        result = oper.mult_oper(value_a,value_b)
    elif operator == '/':
        result = oper.div_oper(value_a,value_b)
    l.changes_prog(value_a, value_b, operator, result, regim) #запись операции
    view.view_data(value_a,value_b,operator,result) # вывод на экран
    button_click()

   



    
    
