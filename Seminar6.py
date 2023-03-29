# # Задача №39. Решение в группах
# # Даны два массива чисел. Требуется вывести те элементы
# # первого массива (в том порядке, в каком они идут в первом
# # массиве), которых нет во втором массиве. Пользователь вводит
# # число N - количество элементов в первом массиве, затем N
# # чисел - элементы массива. Затем число M - количество
# # элементов во втором массиве. Затем элементы второго массива

# # Ввод:                    Вывод:
# # 7                        3 3 2 12
# # 3 1 3 4 2 4 12
# # 6
# # 4 15 43 1 15 1


# import random

# n_size = int(input('Input size of first array: '))
# m_size = int(input('Input size of second array: '))
# array_1 = [random.randint(1, 15) for i in range(n_size)]
# array_2 = [random.randint(1, 15) for i in range(m_size)]
# array_3 = [value for value in array_1 if value not in array_2]
# print(array_1)
# print(array_2)
# print(array_3)


# # Задача №41. Решение в группах
# # Дан массив, состоящий из целых чисел. Напишите
# # программу, которая в данном массиве определит
# # количество элементов, у которых два соседних и, при
# # этом, оба соседних элемента меньше данного. Сначала
# # вводится число N — количество элементов в массиве
# # Далее записаны N чисел — элементы массива. Массив
# # состоит из целых чисел.

# # Ввод:         Ввод:
# # 5             5
# # 1 2 3 4 5     1 5 1 5 1
# # Вывод:        Вывод:
# # 0             2
# # (каждое число вводится с новой строки)

# import random

# n_size = int(input("Input size of array: "))
# array_1 = [random.randint(1,10) for i in range(n_size)]
# counter = 0
# print(array_1)

# for i in range(1, len(array_1) - 1):
#     if array_1[i-1] < array_1[i] and array_1[i+1] > array_1[i]:
#         counter += 1
#         print(f'{i}: {array_1[i]}')

# print(counter)



# # Задача №43. Решение в группах
# # Дан список чисел. Посчитайте, сколько в нем пар
# # элементов, равных друг другу. Считается, что любые
# # два элемента, равные друг другу образуют одну пару,
# # которую необходимо посчитать. Вводится список
# # чисел. Все числа списка находятся на разных
# # строках.


# # Ввод:         Вывод:
# # 1 2 3 2 3     2

# import random
# import math 
# from collections import Counter

# n_size = int(input("Input size of array: "))
# array_1 = [random.randint(0, 10) for i in range(n_size)]
# print(array_1)
# res = Counter()
# for i in array_1:
#     res[i] += 1
# print(res)

# counter = 0
# for k,v in res.items():
#     if v > i:
#         counter += v//2
# print(counter)



# # Задача №45. Решение в группах
# # Два различных натуральных числа n и m называются
# # дружественными, если сумма делителей числа n
# # (включая 1, но исключая само n) равна числу m и
# # наоборот. Например, 220 и 284 – дружественные числа.
# # По данному числу k выведите все пары дружественных
# # чисел, каждое из которых не превосходит k. Программа
# # получает на вход одно натуральное число k, не
# # превосходящее 105
# # . Программа должна вывести все
# # пары дружественных чисел, каждое из которых не
# # превосходит k. Пары необходимо выводить по одной в
# # строке, разделяя пробелами. Каждая пара должна быть
# # выведена только один раз (перестановка чисел новую
# # пару не дает).


# # Ввод:       Вывод:
# # 300         220 284


# import math

# def get_multiplies(number:int) -> list:
#     ls = []
#     for i in range(1,int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             ls.append(i)
#             if not ls.__contains__(number/i) and i!=1:
#                 ls.append(int(number/i))
#     return ls

# limit =100000

# for i in range(1, limit):
#     s = sum(get_multiplies(i))
#     if i == sum(get_multiplies(s)) and i <s:
#         print(f"{i} -> {s}")