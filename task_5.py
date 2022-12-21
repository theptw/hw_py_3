# Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

k = int(input('Введите число: '))


def solution(num):
    fib = [0, 1]
    fib_negative = [1,-1]
    for i in range(2, num + 1):
        fib.append(fib[i-2] + fib[i-1])

    for i in range(2, num):
        fib_negative.append(fib_negative[i-2] - fib_negative[i-1])

    for i in range(len(fib_negative)):
        fib.insert(0, fib_negative[i])
    return fib

print(solution(k))