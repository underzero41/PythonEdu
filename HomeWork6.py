# # Задача 30:  Заполните массив элементами арифметической прогрессии. 
# # Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# # Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# # Каждое число вводится с новой строки.


# first_el = input("Input first element: ")
# diff = input("Input difference: ")
# count = input("Input numbers of element: ")
# array = []

# for i in range(1, int(count) + 1):
#     array.append(int(first_el) + (i - 1) * int(diff))
# print(*array)

# # Задача 32: Определить индексы элементов массива (списка), 
# # значения которых принадлежат заданному диапазону 
# # (т.е. не меньше заданного минимума и не больше заданного максимума)



# import random

# min = int(input("Input start: "))
# max = int(input("Input finish: "))
# array = [random.randint(-10, 11) for _ in range(10)]
# result = []
# print(array)

# for i in range(len(array)):
#     if array[i] >= int(min) and array[i] <= int(max):
#         result.append(i)
# print(result)