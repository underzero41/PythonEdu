# # Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# # Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# # Пользователь вводит 2 числа. 
# # n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# # Затем пользователь вводит сами элементы множеств.

# import random

# first_lenght = input("Input lenght first sequence of numbers: ")
# second_length = input("Input lenght second sequence of numbers: ")

# first_sequence = [random.randint(1, 20) for _ in range(int(first_lenght))]
# second_sequence = [random.randint(1, 20) for _ in range(int(second_length))]

# first_subsequence_set = set(first_sequence)
# second_subsequence_set = set(second_sequence)
# result_sequence = first_subsequence_set.intersection(second_subsequence_set)

# print(first_sequence)
# print(" ")
# print(second_sequence)
# if(len(result_sequence) == 0):
#     print("No match")
# else:
#     print(*sorted(result_sequence))


# # Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# # Она растет на круглой грядке, причем кусты высажены только по окружности. 
# # Таким образом, у каждого куста есть ровно два соседних. 
# # Всего на грядке растет N кустов.
# # Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод –
# # на i-ом кусте выросло ai ягод.
# # В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# # Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# # Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# # собирает ягоды с этого куста и с двух соседних с ним.
# # Напишите программу для нахождения максимального числа ягод,
# # которое может собрать за один заход собирающий модуль, 
# # находясь перед некоторым кустом заданной во входном файле грядки.

# import random

# while(True):
#     number = input("Input number of beds: ")
#     if(number.isdigit() == False or int(number) < 3):
#         print("Input number more then 3: ")
#     else:
#         break

# array = [random.randint(1, 100) for _ in range(int(number))]
# print(array)

# last_element = array[-2]
# last_element_index = -2
# next_element = array[0]
# next_element_index = 0
# temp = array[-2] + array[-1] + array[0]
# result = temp
# result_position = 1
# for i in range(-2, len(array) - 3):
#     next_element = array[next_element_index + 1]
#     next_element_index += 1
#     temp += next_element - last_element
#     last_element = array[last_element_index + 1]
#     last_element_index += 1
#     if result < temp:
#         result = temp
#         result_position = next_element_index
# print("Maximum number of berries: " + str(result) + "\nYou need to start with the bush number: " + str(result_position))
