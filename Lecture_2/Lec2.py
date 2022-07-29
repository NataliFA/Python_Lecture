# Данные. один из способов записи данных

# colors = ['red', 'green', 'blue'] #набор данных: список
# data = open('file.txt', 'a') # текстовая переменная data, путь к файлу, мод с которым работаем, а - добавление)
# # data.writelines(colors) # функционал, позволяющий записать набор данных, разделители записываться не будут
# data.write('LINE 12 \n') #\n - разделитель
# data.write('LINE 13 \n')
# data.close() # необходимо разорвать связь переменной с файлом, чтобы не загружать память
# при 1 запуске создан текстовый файл,при 2 запуске добавлена та же самая И, без разделителей

# 2 способ

# with open('file.txt', 'a') as data:
#     data.write('Line 1 \n')
#     data.write('Line 2 \n')

# чтение данных

# path = 'file.txt'  # путь к файлу
# data = open(path, 'r')  # r - режим чтения
# for line in data:
#     print(line) # так же делает переход на новую строку, поэтому двойные пустые строки
# data.close()

# exit()  # позволяет не использовать код, указанный ниже

# Функции

# import Function as F
# print(F.f(1))

# def new_string(symbol, count = 3): #если значение явно не указывается, то по умолчанию = 3
#     return symbol * count

# # print(new_string('!', 7)) # !!!!!!!
# print(new_string('!')) # Error, если значение явно не указано
# print(new_string(4)) # 12

# возможность передачи неограниченного числа аргументов, для этого перед аргументом *

# def concatenatio(*params):
#     # res: str = ""
#     res = 0 #: int = 0
#     for item in params:
#         res += item
#     return res

# # print(concatenatio('a', 's', 'd', 'w')) # asdw
# # print(concatenatio('a', '1')) # a1
# print(concatenatio(1, 2, 3, 4)) # TypeError: так как функция описывает работу со строками (указан тип данных str), а не с числами

# Рекурсия. Фибоначчи

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)  # 1 1 2 3 5 8 13

# Негафибоначчи. отрицательные числа

# def fib(n):
#     if n in [-1]:
#         return 1
#     elif n in [-2]:
#         return -1
#     else:
#         return fib(n+2) - fib(n+1)


# list = []
# for e in range(-10, 0):
#     list.append(fib(e))
# print(list)

# Кортежи

# a, b = 3, 4 # множественное присваивание

# a = (3, 4, 5, 12)  # со скобками - кортеж, необязательно использовать 2 переменных
# print(a)
# print(a[-1])  # можно обращаться к конкретному элементу

# t = ()
# print(type(t))  # tuple
# t = (1,)
# print(type(t))  # tuple
# t = (1)
# print(type(t))  # int
# t = (28, 9, 1990)
# print(type(t))  # tuple

# colors = ['red', 'green', 'blue']
# print(colors)  # ['red', 'green', 'blue']
# t = tuple(colors) # превратить список в кортеж
# print(t)

# t = tuple(['red', 'green', 'blue'])
# print(t[0])  # red
# print(t[2])  # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2])  # green
# # print(t[-200]) # IndexError: tuple index out of range

# for e in t:
#     print(e)  # red green blue

# двойное преобразование

# t = tuple(['red', 'green', 'blue']) # список превращаем в кортеж
# red, green, blue = t # распаковываем список, превращаем в 3 независимых переменных
# print('r:{} g:{} b:{}'.format(red, green, blue))

# Словари

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',  # ключ, значение
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }  # слеш для того, чтобы не писать все значения в 1 строчку

# print(dictionary['up'])
# dictionary['up'] = 'upper' # изменили значение ключа
# print(dictionary['up'])
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←

# for k in dictionary.keys():
#     print(k)
# # то же самое (ключи)
# for k in dictionary:
#     print(k)

# for v in dictionary.values():
#     print(v)
# # то же самое (значения)
# for v in dictionary:
#     print(dictionary[v])

# del dictionary['left']  # удаление элемента
# for item in dictionary:  # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))

# Множества

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'} type - set
# colors.add('red') # если есть такой элемент, то не добавит
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray') # добавит элемент в конец
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # удалить элемент
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') так как элемента уже нет, то возникнет ошибка
# colors.discard('red') # если элемент уже удален, то программа продолжит работу
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } очистить множество
# print(colors) # set()

# пересечение, объединение, разность, симметрическая разность и т.д.

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}

# c = a.copy() # c = {1, 2, 3, 5, 8} создать множество на основе имеющегося
# print(c)

# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} множество а объединить с b
# print(u)

# i = b.intersection(a) # i = {8, 2, 13, 5}
# print(i)

# dl = a.difference(b) # dl = {1, 3}
# print(dl)
# dr = b.difference(a) # dr = {13, 21}
# print(dr)

# q = a \
#    .union(b) \
#    .difference(a.intersection(b))
# print(q)

# неизменяемое множество

# a = {1, 2, 3, 5, 8}
# b = frozenset(a) #методы удаления, добавления и т д работать не будут
# print(b) # frozenset({1, 2, 3, 5, 8})

# Списки

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123 # меняя значения 1 списка также меняется значение и 2 списка
# list2[1] = 333 # и наоборот
# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1 = [6, 5, 4, 3, 2, 1]
# print(len(list1))
# print(list1.pop())  # удаление последнего элемента
# print(list1)
# print(len(list1))
# print(list1.pop(2)) # удалит 2 элемент
# print(list1)

# print(list1.insert(2, 11)) # вставит элемент 11 на 2 позицию (м/у 5 и 4), чтобы добавить элемент в конец .append(эл-т)
# print(list1)

