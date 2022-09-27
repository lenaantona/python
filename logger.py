from datetime import datetime as d

def changes_prog(num1, num2, oper, result, regim): #запись производимых операций калькулятором
    time_changes = d.now().strftime('%D %H:%M')
    f_changes = 'log.csv'
    f = open(f_changes, 'a', encoding="utf-8")
    f.write(f'{regim} режим:{num1} {oper} {num2} = {result} =>({time_changes})\n')
    f.close()

def exit_prog(): #запись при закрытии программы
    time_changes = d.now().strftime('%D %H:%M')
    f_changes = 'log.csv'
    f = open(f_changes, 'a', encoding="utf-8")
    f.write(f'Программа закрыта=>({time_changes})\n')
    f.close()

def input_error(message): #запись ошибок ввода
    time_changes = d.now().strftime('%D %H:%M')
    f_changes = 'log.csv'
    f = open(f_changes, 'a', encoding="utf-8")
    f.write(f'Сообщение ошибки ввода: {message} =>({time_changes})\n')
    f.close()