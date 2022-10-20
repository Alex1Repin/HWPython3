# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonacci(n):
    fibonacci = [0, 1]
    nega_fibonacci = [1, 0]

    for i in range(2, n + 1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        nega_fibonacci.insert(0, nega_fibonacci[1] - nega_fibonacci[0])

    nega_fibonacci.extend(fibonacci[1:])
    return nega_fibonacci
print(Fibonacci(8))