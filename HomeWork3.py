import random
# # Задача 16: Требуется вычислить, сколько раз встречается некоторое
# # число X в массиве A[1..N].
# # Пользователь в первой строке вводит
# # натуральное число N – количество элементов в массиве. В последующих
# # строках записаны N целых чисел Ai
# # . Последняя строка содержит число X
# # 5
# # 1234 5
# # 3 -> 1


# N = input ('Input size of array: ')
# array_1 = [random.randint(-10, 10) for _ in range(int(N))]
# print(array_1)
# find = input('Find number: ')

# dictionary = {}

# for i in range(len(array_1)):
#     if dictionary.get(array_1[i]) == None:
#         dictionary[array_1[i]] = 1
#     else:
#         dictionary[array_1[i]] += 1

# print(f'Number {find} -> {dictionary[int(find)]}')



# # Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# # Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# # В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# # 5
# # 1234 5
# # 6 -> 5

# N = input("Input size of array: ")
# array_1 = [random.randint(1, 40) for _ in range(int(N))]
# print(array_1)
# find = input("Input number which we are looking for: ")

# result = array_1[0]
# temp = abs(int(find) - array_1[0])

# for i in range(len(array_1) - 1):
#     if abs(int(find) - array_1[i + 1]) < temp:
#         temp = abs(int(find) - array_1[i + 1])
#         result = array_1[i + 1]
#         if temp == abs(int(find) - array_1[i + 1] and result > array_1[i + 1]):
#             result = array_1[i + 1]

# print(f'{find} -> {str(result)}')



# # Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# # В случае с английским алфавитом очки распределяются так:
# # ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# # ● D, G – 2 очка;
# # ● B, C, M, P – 3 очка;
# # ● F, H, V, W, Y – 4 очка;
# # ● K – 5 очков;
# # ● J, X – 8 очков;
# # ● Q, Z – 10 очков.
# # А русские буквы оцениваются так:
# # ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# # ● Д, К, Л, М, П, У – 2 очка;
# # ● Б, Г, Ё, Ь, Я – 3 очка;
# # ● Й, Ы – 4 очка;
# # ● Ж, З, Х, Ц, Ч – 5 очков;
# # ● Ш, Э, Ю – 8 очков;
# # ● Ф, Щ, Ъ – 10 очков.
# # Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# # Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# # либо только русские буквы.

# def Check_Language(language):
#     result = 0
#     for i in word.upper():
#         result += language[i]
#     return result

# language = input("Choose the language, print 'ru' or 'en': ")
# word = input("Write the word: ")

# en_dict = {'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1, 'U' : 1, 'L' : 1, 'N' : 1,
#             'S' : 1, 'T' : 1, 'R' : 1,'D' : 2, 'G' : 2,  'B' : 3, 'C' : 3, 'M' : 3, 'P' : 3,
#             'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4, 'Y' : 4,  'K' : 5,  'J' : 8, 'X' : 8,  'Q' : 10, 'Z' : 10}

# ru_dict = {'А' : 1, 'В' : 1, 'Е' : 1, 'И' : 1, 'Н' : 1, 'О' : 1, 'Р' : 1, 'С' : 1, 'Т' : 1,
#            'Д' : 2, 'К' : 2, 'Л' : 2, 'М' : 2, 'П' : 2, 'У' : 2, 'Б' : 3, 'Г' : 3, 'Ё' : 3, 
#            'Ь' : 3, 'Я' : 3,'Й' : 4, 'Ы' : 4,'Ж' : 5, 'З' : 5, 'Х' : 5,
#             'Ц' : 5, 'Ч' : 5,'Ш' : 8, 'Э' : 8, 'Ю' : 8,'Ф' : 10,'Щ' : 10, 'Ъ' : 10}

# if(language == "en"):
#     print(f'{word} -> {Check_Language(en_dict)}')
# elif(language == "ru"):
#     print(f'{word} -> {Check_Language(ru_dict)}')
# else:
#     print('Error 404, you have mistake, on choosing language')
