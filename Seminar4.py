# # Задача №25. Решение в группах
# # Напишите программу, которая принимает на вход
# # строку, и отслеживает, сколько раз каждый символ
# # уже встречался. Количество повторов добавляется к
# # символам с помощью постфикса формата _n.
# # Input: a a a b c a a d c d d
# # Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# # Для решения данной задачи используйте функцию
# # .split()

# letters = 'a a a b c a a d c d d'
# dict_letters = {}
# result_string = ''

# letters = letters.split(' ')
# print(letters)
# for i in range(len(letters)):
#     if dict_letters.get(letters[i]) == None:
#         dict_letters[letters[i]] = 0
#         result_string +=f'{letters[i]} '

#     else:
#         dict_letters[letters[i]] += 1
#         result_string += f'{letters[i]}_{dict_letters[letters[i]]} '

# print(result_string)


# # Задача №27. Решение в группах
# # Пользователь вводит текст(строка). Словом считается
# # последовательность непробельных символов идущих
# # подряд, слова разделены одним или большим числом
# # пробелов. Определите, сколько различных слов
# # содержится в этом тексте.
# # Input: She sells sea shells on the sea shore The shells
# # that she sells are sea shells I'm sure.So if she sells sea
# # shells on the sea shore I'm sure that the shells are sea
# # shore shells
# # Output: 13

# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# dict = {}
# result = 0

# splited_text = text.lower().split(' ')

# for i in range(len(splited_text)):
#     if dict.get(splited_text[i]) == None:
#         dict[splited_text[i]] = 1
#         result += 1
# print(result)

# # Задача №29. Решение в группах
# # Ваня и Петя поспорили, кто быстрее решит
# # следующую задачу: “Задана последовательность
# # неотрицательных целых чисел. Требуется определить
# # значение наибольшего элемента
# # последовательности, которая завершается первым
# # встретившимся нулем (число 0 не входит в
# # последовательность)”. Однако 2 друга оказались не
# # такими смышлеными. Никто из ребят не смог до
# # конца сделать это задание. Они решили так: у кого
# # будет меньше ошибок в коде, тот и выиграл спор. За
# # помощью товарищи обратились к Вам, студентам.
# # Ваня:
# n = int(input())
# max_number = -1
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)

# # Петя:
# n = int(input())
# max_number = -1
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number) 
