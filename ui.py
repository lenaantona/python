def view(list):
    '''
    Функция принимает на вход лист c листами строк и выводит каждую с новой строки на экран
    '''
    str1 = ''
    for line in list:
        str1 = str1 + ','.join(line)+'\n'
    return str1

