# Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) 
# чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def input_num():
    correct = False
    while not correct:
        try:
            num = int(input('Введите вещественное число:\n'))
            correct = True
        except ValueError:
                print('Не является числом"\n')
    return num   
n = input_num()
list_factorial = []
res = 1
for i in range(1, n+1):
    res = res * i
    list_factorial.append(res)
print(list_factorial)