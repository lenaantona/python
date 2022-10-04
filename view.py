global s
s  = ''
def view_data(oper,a,b, res): # ввывод результата
    s = ''
    if oper == '-':
        s = '{} - {} = {}'.format(a,b,res)
    elif oper == '+':
        s = '{} + {} = {}'.format(a,b,res)
    elif oper == '*':
        s = '{} * {} = {}'.format(a,b,res)
    elif oper == '/':
        s = '{} / {} = {}'.format(a,b,res)
    return s

def get_regime(r): # вывод  режима на экран
    if r == '1':
        s = 'Вы выброли режим: комлексные числа'
    elif r == '2':
        s = 'Вы выброли режим: рациональные числа'
    return s
