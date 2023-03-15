# # Task 10: На столе лежат n монеток. Некоторые из них лежат вверх
# # решкой, а некоторые – гербом. Определите минимальное число
# # монеток, которые нужно перевернуть, чтобы все монетки были
# # повернуты вверх одной и той же стороной. Выведите минимальное
# # количество монет, которые нужно перевернуть.
# # 5 -> 1 0 1 1 0

# import random

# while True:
#     n = input('Input quantity of coins: ')
#     if(n.isdigit() == False):
#         print('Input numbers, not chars')
#     elif(int(n) <= 0):
#         print('Quanity of coins must be > 0')
#     else:
#         break

# coin = list()

# for i in range(int(n)):
#     coin.append(random.randint(0,1))

# if(coin.count(1) < coin.count(0)):
#     print(n, ' -> ', *coin)
#     print(coin.count(1))
# elif(coin.count(1) == coin.count(0)):
#     print(n, ' -> ', *coin)
#     print('no difference')
# else:
#     print(n, ' -> ', *coin)
#     print(coin.count(0))



# # Task 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# # школьница. Петя помогает Кате по математике. Он задумывает два
# # натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# # этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# # произведение P. Помогите Кате отгадать задуманные Петей числа.
# # 4 4 -> 2 2
# # 5 6 -> 2 3

# x = input('Input X: ')
# y = input('Input Y: ')
# x, y = map(int, (x,y))
# flag = False
# for i in range(x + y):
#     if flag:
#         break
#     for j in range(x + y):
#         if i + j == x and i * j == y:
#             flag = True
#             print(x, y, ' -> ', *sorted([i, j]))
#             break



# # Task 14: Требуется вывести все целые степени двойки (т.е. числа
# # вида 2 в степени k), не превосходящие числа N.
# # 10 -> 1 2 4 8

# while(True):
    
#     n = input("Input number: ")
#     if(n.isdigit() == False or int(n) < 1):
#         print("Input number: ")
#     else:
#         break
    
# i = 0
# temp = 0
# result = []

# while(int(temp) <= int(n)):

#     if((2 ** i) <= int(n)):
#         result.append(2 ** i)
#         temp = result[i]
#         i = i + 1
#     else:
#         break

# print(n, ' -> ', *result)