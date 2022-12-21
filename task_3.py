# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

my_list = []

for i in range(10):
    index = random.randint(0,3)
    my_list.append(round(random.uniform(0,10), index))
print(my_list)

def solution(list):
    maxproc = my_list[0] % 1
    minproc = my_list[len(my_list)-1] % 1
    for i in range(len(my_list)):
        if my_list[i] % 1 > maxproc and my_list[i] % 1 > 0:
            maxproc = my_list[i] % 1
        if  my_list[i] % 1 < minproc and my_list[i] % 1 > 0:
            minproc = my_list[i] % 1
    return round(maxproc - minproc, 3)

print(solution(my_list))

    