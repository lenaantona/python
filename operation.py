# Вариант игры с ботом (с интеллектом)
global str_mes
str_mes =''

def oper(count, ostatok):
    res = []
    try:
        count = int(count)
        if count > 28 or count > ostatok: 
            str_mes ='Нельзя взять больше 28 конфет, либо кол-во конфет больше чем осталось! Введите еще раз:'
            ostatok = 0
        else:
            ostatok = ostatok - count
            str_mes ='Осталось конфет {}'.format(ostatok)
    except: 
        str_mes ='это не число, введите число'
        ostatok = 0
    res.append(str_mes)
    res.append(ostatok)
    return res

def oper_res(count, ostatok):
    count = int(count)
    result = []
    if ostatok > 30: 
        count = 30 - count
        ostatok = ostatok - count
        str_mes ='Бот взял {} конфет, всего осталось {} конфет, Ваш ход'.format(count, ostatok)
    else: # случай для последнего хода
        count = ostatok - 1
        ostatok = ostatok - count
        str_mes='Бот взял {} конфет, осталось {} конфет, Вы проиграли.Для новой игры нажми /new'.format(count, ostatok)
    result.append(str_mes)
    result.append(ostatok)
    return result
