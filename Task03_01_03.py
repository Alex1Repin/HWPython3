# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной 
# части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input('Введите количество чисел n: '))
lst = []
new_list = []
for i in range(n):
    lst.append(float(input('float -->')))

for i in range(len(lst)):
    n = lst[i] % 1
    if n != 0:
        new_list.append(n)
minb = min(new_list)
maxb = max(new_list)
print(maxb - minb)
