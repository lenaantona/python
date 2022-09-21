# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, 
# написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер,
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
list_program = ['python', 'c#', 'java', 'c++', 'php', 'c', 'javascript', 'arduino']
list_numbers = [i for i in range(1, len(list_program)+1)]
list_program = list(map(lambda i: i.upper(), list_program))
new_list = list(zip(list_numbers, list_program))
result_list = []

def sum_char_kod(input_list):
    sum = 0
    for i in str(input_list[1]):
        sum += ord(i)
    if (sum % int(input_list[0]) == 0):
        return (str(sum), input_list[1])

result = list(map(lambda i: sum_char_kod(i), new_list))
for i in range(len(result)):
    try:
        result.remove(None)
    except: 
        continue

print(result)

