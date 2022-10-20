# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from ctypes import RTLD_LOCAL
from random import randint

def numbers(n): 
    numbers = [randint(-n, n)]
    for i in range(1, n):
        numbers.append(randint(-n, n))
    return numbers

roll = numbers(10)
print(roll)
sum = 0
for i in range(len(roll)):
    if i % 2 != 0:
        sum += roll[i]
print(sum)
