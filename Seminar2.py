# # Task №9. Решение в группах
# # По данному целому неотрицательному n вычислите
# # значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# # чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# # while
# # Input: 5
# # Output: 120

# n = int(input('Write N: '))
# res = 1
# i = 1
# if n < 0:
#     print('Input a non-negative number')
# else:
#     while i <= n:
#         res *= i
#         i += 1
   
#     print(res)


# # Task №11. Решение в группах
# # Дано натуральное число A > 1. Определите, каким по
# # счету числом Фибоначчи оно является, то есть
# # выведите такое число n, что φ(n)=A. Если А не
# # является числом Фибоначчи, выведите число -1.
# # Input: 5
# # Output: 6

# n = int(input('Input number: '))
# a = 0
# b = 1
# counter = 1

# if n == 0:
#     print(counter)

# else:
#     while(a < n):
#         a, b = b, a + b
#         counter += 1
        
#     if n == a:
#         print(f'Number is on position {counter}')
#     else:
#         print('There is NO Fibbo number')        



# # Task №13. Решение в группах
# # Уставшие от необычно теплой зимы, жители решили узнать,
# # действительно ли это самая длинная оттепель за всю историю
# # наблюдений за погодой. Они обратились к синоптикам, а те, в
# # свою очередь, занялись исследованиями статистики за
# # прошлые годы. Их интересует, сколько дней длилась самая
# # длинная оттепель. Оттепелью они называют период, в
# # который среднесуточная температура ежедневно превышала
# # 0 градусов Цельсия. Напишите программу, помогающую
# # синоптикам в работе.
# # Пользователь вводит число N – общее количество
# # рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# # располагается N целых чисел.
# # Каждое число – среднесуточная температура в
# # соответствующий день. Температуры – целые числа и лежат в
# # диапазоне от –50 до 50
# # Input: 6 -> -20 30 -40 50 10 -10
# # Output: 2

# import random

# days = input('Input how many days: ')
# temperature = list()
# temp = 0 
# resultTemp = 0

# for i in range(int(days)):
#     temperature.append(random.randint(-50, 50))

# print(temperature)
# for i in range(int(days)):
#     if(int(temperature[i] > 0)):
#         resultTemp += 1
#     else:
#         if(resultTemp > temp):
#             temp = resultTemp
#         resultTemp = 0

# print(temp)




# # Task №15. Решение в группах
# # 15. Иван Васильевич пришел на рынок и решил
# # купить два арбуза: один для себя, а другой для тещи.
# # Понятно, что для себя нужно выбрать арбуз
# # потяжелей, а для тещи полегче. Но вот незадача:
# # арбузов слишком много и он не знает как же выбрать
# # самый легкий и самый тяжелый арбуз? Помогите ему!
# # Пользователь вводит одно число N – количество
# # арбузов. Вторая строка содержит N чисел,
# # записанных на новой строчке каждое. Здесь каждое
# # число – это масса соответствующего арбуза
# # Input: 5 -> 5 1 6 5 9
# # Output: 1 9

# import random

# n = input('How much watermelons? ')
# wm_weight = list()

# for i in range(int(n)):
#     wm_weight.append(random.randint(1,10))

# min = wm_weight[0]
# max = wm_weight[1]
# # print(wm_weight)

# for i in range(int(n)):
#     if(wm_weight[i] < min):
#         min = wm_weight[i]
#     if(wm_weight[i] > max):
#         max = wm_weight[i]

# print(f'For techcha {min} for me {max}')