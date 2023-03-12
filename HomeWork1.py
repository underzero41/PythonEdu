# # Task 2: Найдите сумму цифр трехзначного числа.
# # 123 -> 6 (1 + 2 + 3)
# # 100 -> 1 (1 + 0 + 0) 

# while True:
#     number = (input('Write a number: '))
#     if number.isdigit() == False:
#         print('Error 404')
#     if len(number) > 3 or len(number) < 3:
#         print('error 404')
#     else:
#         break

# a = int(number) //100
# b = (int(number) //10) %10
# c = int(number) %10
# sum = a + b + c
# print(f'{number} -> {sum} -> ({a}+{b}+{c})')



# # Task 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# # Вместе они сделали S журавликов. 
# # Сколько журавликов сделал каждый ребенок, если известно, 
# # что Петя и Сережа сделали одинаковое количество журавликов, 
# # а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# # 6 -> 1  4  1
# # 12 -> 2  8  2
# # 18 -> 3  12   3
# # 24 -> 4  16  4
# # 60 -> 10  40  10

# while True:
#     number = (input('How many cranes: '))
#     if number.isdigit() == False:
#         print('Input numbers, not chars!')
    
#     if int(number)%6 != 0:
#         print('Input multiple of six')
#     else:
#         break

# num = int(number) / 6
# num2 = (int(num) + int(num)) * 2

# print(f'{int(number)} -> {int(num)}  {int(num2)}  {int(num)}')


# Task 6 : Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# while True:
#     number = (input('Write a number: '))
#     if number.isdigit() == False:
#         print('Error 404')
#     if len(number) != 6:
#         print('error 404, input six-digit number')
#     else:
#         break

# a = int(number[0])
# b = int(number[1])
# c = int(number[2])
# d = int(number[3])
# e = int(number[4])
# f = int(number[5])

# # print(b)

# sum1 = a + b + c
# sum2 = d + e + f

# if sum1 == sum2:
#     print(f'{number} -> yes')
# else:
#     print('Do not give up')



# # Task 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# # если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# # 3 2 4 -> yes
# # 3 2 1 -> no

# while True:
#     n = (input('Write n: '))
#     m = (input('Write m: '))
#     k = (input('Write k: '))

#     if n.isdigit() == False or m.isdigit() == False or k.isdigit() == False:
#         print('Error 404, input numbers')
#     else:
#         break

# if(int(n) * int(m) == int(k)):
#     print('Take whole chocolate bar')
# elif (int(k) > int(n) * int(m) or int(k) <= 0):
#     print('There are not so many slices')
# elif (int(n) == int(k) or int(m) == int(k) or int(k) % int(n) == 0 or int(k) % int(m) == 0):
#     print(n, m, k, ' -> yes')
# else:
#     print(n, m, k, ' -> no')