# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

new_str = input('Введите текст :')

def delete_abv(input_str):
    old_list = input_str.split(' ')
    new_list = list(filter(lambda i: 'абв' not in i, old_list))
    result_str = ' '.join(new_list)
    return result_str

str1 = delete_abv(new_str)
print('Текст после удаления абв:' + str1)