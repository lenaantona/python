# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.
def squeeze_text():
    '''
    считывает из файла текст, сжимает и записывает в другой файл
    '''
    str1 = ''
    with open('old_text.txt', 'r', encoding="utf-8") as f1: # считывание из файла
        str1 = f1.read()
    print(str1)
    str_code = ''
    count = 1
    last_st = ''
    for i in range(0, len(str1)): #формирует сжатую строку
        try:
            last_st = str1[i + 1]
        except IndexError:
            last_st = str1[i - 2]

        if str1[i] == last_st:
            count += 1
        else:
            str_code = str_code + str1[i] + str(count)
            count = 1
    with open('new_text.txt', 'w', encoding="utf-8") as f2: #записывает сжатый текст в файл
        f2.write(str_code)
    print(str_code) 

def is_number(st):
    '''
    проверяет является символ строки числом
    '''
    try:
        int(st)
        return True
    except ValueError:
        return False

def reestablish():
    '''
    считывает сжатый текст и восстанавливает
    '''
    str1 = ''
    with open('new_text.txt', 'r', encoding="utf-8") as f1: #считывает сжатый текст
        str1 = f1.read()
    new_list =[]
    i = 0
    while i < len(str1):  # формирует из строки список, где поочередно символ и кол-во повторений
        if is_number(str1[i]) == False:  # если символ добавляем в список
            new_list.append(str1[i])
            i += 1
        else: 
            str2 = ''
            while (i < len(str1) and is_number(str1[i]) == True): # если цифра, то сначала собираем из близ лежащих число, а потом добавляем в список 
                str2 += str1[i]
                i += 1
            new_list.append(int(str2))
    str_result = ''
    j = 0
    while j < len(new_list):  # преобразует список в строку
        str_result += new_list[j] * new_list[j+1]
        j += 2
    return(str_result) 

squeeze_text()
print(reestablish())




