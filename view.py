def view_data(a,b,op,res): # ввывод результата
    print(f'{a} {op} {b} = {res}') 

def get_value(): # получение 1 и 2 числа
    return input('Введите число = ')

def get_regime(): # получение режима
    return input('Введите режим работы калькулятора:\n 1 - реляционные числа,\n 2 - комплексные числа,\n 0 - закрыть программу\n')

def get_operations(): # получение операции
    return input('Введите операцию(+,-,/,*) = ')