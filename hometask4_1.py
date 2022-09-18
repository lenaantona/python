# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
def input_num():
    correct = False
    while not correct:
        try:
            num = int(input('Введите целое число:\n'))
            correct = True
        except ValueError:
                print('Не является числом"\n')
    return num   


def prime_factors(n):
    num = n
    simpl_n = 2
    new_set = set()
    while n > 1:
        while simpl_n <= num:
            if n % simpl_n == 0: 
                new_set.add(simpl_n)
                n = n/simpl_n
            else: simpl_n+=1
    return new_set

numbers = input_num()
print(prime_factors(numbers))        
 