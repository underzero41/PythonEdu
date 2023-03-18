import random

# # Задача №17. Решение в группах
# # Дан список чисел. Определите, сколько в нем
# # встречается различных чисел.
# # Input: [1, 1, 2, 0, -1, 3, 4, 4]
# # Output: 6

# list_1 = [random.randint(-10,10) for _ in range(random.randint(5,10))]
# print(list_1)
# set_1 = set(list_1)
# length = len(set_1)
# print(set_1)
# print(length)


# # Задача №19. Решение в группах
# # Дана последовательность из N целых чисел и число
# # K. Необходимо сдвинуть всю последовательность
# # (сдвиг - циклический) на K элементов вправо, K –
# # положительное число.
# # Input: [1, 2, 3, 4, 5] k = 3
# # Output: [4, 5, 1, 2, 3]

# array_length = input('Input size of array: ')
# k = input('Input size of the step: ')
# list_1 = [random.randint(-100, 100) for _ in range(int(array_length))]
# print(list_1)

# # for i in range(int(k)):
# #     list_1.insert(0, list_1.pop())

# # print(list_1)
# print(list_1[int(k) * - 1:] + list_1[:len(list_1) - int(k)])


# # Задача №21. Решение в группах
# # Напишите программу для печати всех уникальных
# # значений в словаре.
# # Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# # {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# # ":" S007 "}]
# # Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# array_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII" : "S007"}]
# print(array_1)
# unique_dict = {}

# for i in range(len(array_1)):
#     for j in array_1[i].values():
#         unique_dict[j] = "None"

# print('{', *unique_dict.keys(), '}')

# # Задача №23. Решение в группах
# # Дан массив, состоящий из целых чисел. Напишите
# # программу, которая подсчитает количество
# # элементов массива, больших предыдущего (элемента
# # с предыдущим номером)
# # Input: [0, -1, 5, 2, 3]
# # Output: 2 (-1 < 5, 2 < 3)

# nums = input('Input size of array: ')
# array_1 = [random.randint(-10, 10) for _ in range(int(nums))]
# counter = 0
# resulting_string = ''
# print(array_1)

# for i in range(len(array_1) - 1):
#     if(array_1[i] < array_1[i + 1]):
#         counter += 1
#         resulting_string += f'{array_1[i]} < {array_1[i + 1]}  '

# print(f'{counter} ({resulting_string})')
