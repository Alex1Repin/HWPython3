# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и
# т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint

def numbers(n): 
    numbers = [randint(0, n)]
    for i in range(1, n):
        numbers.append(randint(0, n))
    return numbers

roll = numbers(5)
print(roll)
new_list = []
for i in range(len(roll)//2 + len(roll)%2):
    new_list.append(roll[i] * roll[-i-1])
print(new_list)

