# # Задача №47. Решение в группах
# # У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# # программы используется множество раз и вы не хотите ничего сломать):
# # transformation = <???>
# # values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# # transormed_values = list(map(transformation, values))
# # Единственный способ вашего взаимодействия с этим кодом - посредством задания
# # функции transformation.
# # Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# # список значений, а нужно получить его как есть.
# # Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# # копией values.
# # Ввод:
# # values = [1, 23, 42, ‘asdfg’]
# # transformed_values = list(map(trasformation, values))
# # if values == transformed_values:
# #  print(‘ok’)
# # else:
# #  print(‘fail’)
# # Вывод:
# # ok

# # transformation = <???>
# # values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# # transormed_values = list(map(transformation, values))

# transformation =  lambda x: x
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#  print('ok')
# else:
#  print('fail')


# # Задача №49. Решение в группах
# # Планеты вращаются вокруг звезд по эллиптическим орбитам.
# # Назовем самой далекой планетой ту, орбита которой имеет
# # самую большую площадь. Напишите функцию
# # find_farthest_orbit(list_of_orbits), которая среди списка орбит
# # планет найдет ту, по которой вращается самая далекая
# # планета. Круговые орбиты не учитывайте: вы знаете, что у
# # вашей звезды таких планет нет, зато искусственные спутники
# # были были запущены на круговые орбиты. Результатом
# # функции должен быть кортеж, содержащий длины полуосей
# # эллипса орбиты самой далекой планеты. Каждая орбита
# # представляет из себя кортеж из пары чисел - полуосей ее
# # эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# # где a и b - длины полуосей эллипса. При решении задачи
# # используйте списочные выражения. Подсказка: проще всего
# # будет найти эллипс в два шага: сначала вычислить самую
# # большую площадь эллипса, а затем найти и сам эллипс,
# # имеющий такую площадь. Гарантируется, что самая далекая
# # планета ровно одна
# # Ввод:
# # orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# # print(*find_farthest_orbit(orbits))
# # Вывод:
# # 2.5 10

# import math
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# # print(*find_farthest_orbit(orbits))

# print(orbits)
# print(*max(orbits, key= lambda x: math.pi*x[0]*x[1] if x[0]!= x[1] else 0))

# maxorboit = 0
# index_maxorbit = 0
# for i in range(len(orbits)):
#     print('a =', orbits[i][0], 'b =', orbits[i][1])
#     length_orbit = 0
#     if orbits[i][0] != orbits[i][1]:
#         length_orbit = math.pi*orbits[i][0]*orbits[i][1]
#     if length_orbit > maxorboit:
#         maxorboit = length_orbit
#         index_maxorbit = i
# print(*orbits[index_maxorbit])

# print('--------------------')

# print(orbits)
# print(*max(orbits, key= lambda x: math.pi*x[0]*x[1] if x[0]!= x[1] else 0))

# maxorboit = 0
# index_maxorbit = 0
# for i in orbits: # lambda x
#     print('a =', i[0], 'b =', i[1])
#     length_orbit = 0 # else 0
#     if i[0] != i[1]: # if x[0]!= x[1]
#         length_orbit = math.pi*i[0]*i[1] # math.pi*x[0]*x[1]
#     if length_orbit > maxorboit:  # max()
#         maxorboit = length_orbit
#         index_maxorbit = i
# print(*index_maxorbit)

# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# values = [0, 2, 10, 6]
# def same_by(func, input_values):
#     result = list(map(func, input_values))
#     return min(result) == max(result)    

# print(same_by(lambda x: x % 2, values))

# # values = [0, 2, 10, 6]
# # if same_by(lambda x: x % 2, values):
# #     print("same")
# # else:
# #     print("different")

