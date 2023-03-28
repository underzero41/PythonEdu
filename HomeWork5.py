# # Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# # и возводит число А в целую степень B с помощью рекурсии.

# # *Пример:*

# # A = 3; B = 5 -> 243 (3⁵)
# #     A = 2; B = 3 -> 8 

# def degree(first_num, second_num):
#     if second_num == 1:
#         return first_num
#     return int(first_num) * degree(int(first_num), int(second_num) - 1)

# first_number = input("Input number: ")
# second_number = input("Input degree: ")

# print(f"A = {first_number}; B = {second_number} -> " + str(degree(first_number, second_number)))



# # Задача 28: Напишите рекурсивную функцию sum(a, b), 
# # возвращающую сумму двух целых неотрицательных чисел. 
# # Из всех арифметических операций допускаются только +1 и -1. 
# # Также нельзя использовать циклы.

# # *Пример:*
# # 2 2
# # 4

# def sum(first_num, second_num):
    
#     if int(second_num) == 0:
#         return int(first_num)
#     return 1 + sum(first_num, second_num - 1)

# first_num = int(input('Input first number: '))
# second_num = int(input('Input second number: '))
# print(sum(first_num, second_num))