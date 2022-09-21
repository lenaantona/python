# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг
#  после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет
# (или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
def input_num():
    correct = False
    while not correct:
        try:
            num = int(input('Введите кол-во конфет на столе:\n'))
            if num < 30: 
                print ('Кол-во конфет не может быть меньше 30: ')
            else:
                correct = True
        except ValueError:
                print('Не является числом"\n')
    return num  
    
ostatok = input_num() # кол-во конфет
gamer1 = 'Игрок1'
gamer2 = 'Игрок2'
b = True

while ostatok >= 1:
    if b == True:
         gamer = gamer1
    else: gamer = gamer2 
    if ostatok == 1: 
        print(gamer+', осталась 1 конфета, Вы проиграли')
        ostatok -= 1
    else:
        try:
            count = int(input(gamer+' введите кол-во конфет: '))
            if count > 28 or count > ostatok: 
                print ('Нельзя взять больше 28 конфет, либо кол-во конфет больше чем осталось!')
                continue
            ostatok = ostatok - count
            print(f'Осталось конфет {ostatok}')
        except: print('это не число, пропускаете ход')
    b = not b



#Вариант игры с ботом (с интеллектом)
# fersthod = 0
# ostatok = input_num()
# fersthod = ostatok - int(ostatok/30) * 30
# while ostatok >1:
#     if fersthod > 0: # для первого хода (убрать остаток)
#         ostatok -= fersthod
#         print(f'Бот забрал {fersthod} конфет, осталось конфет {ostatok}')
#         fersthod = -1
#     elif fersthod == 0: 
#         print(f'Бот уступает Вам ход')
#         fersthod = -1 # чтобы больше не выполнялось действие
#     try:
#         count = int(input('Введите кол-во конфет: '))
#         if count > 28 or count > ostatok: 
#             print ('Нельзя взять больше 28 конфет, либо кол-во конфет больше чем осталось!')
#             continue
#         ostatok = ostatok - count
#         print(f'Осталось конфет {ostatok}')
#     except: 
#         print('это не число')
#         continue
#     if ostatok > 30: 
#         count = 30 - count
#         ostatok = ostatok - count
#         print(f'Бот взял {count} конфет, всего осталось {ostatok} конфет')
#     else: # случай для последнего хода
#         count = 30 - count - 1
#         ostatok = ostatok - count
#         print(f'Бот взял {count} конфет, осталось {ostatok} конфет, Вы проиграли')





