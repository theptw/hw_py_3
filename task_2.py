# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = [1, 6, 3, 4, 4, 5, 1, 2, 3]
b = len(my_list) - 1
for i in range(len(my_list)//2 + 1):
    print(f'{my_list[i] * my_list[b]} - произведение {i+1} пары')
    b -= 1