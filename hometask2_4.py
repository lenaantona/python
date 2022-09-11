# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) 
# - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)
import time

def random_min_max(min, max):
    raz = max - min
    misecond = (time.time_ns()%10**8)/10**8
    num = min + round(misecond * raz)
    print(misecond)
    return num

print(random_min_max(-10, 100))

