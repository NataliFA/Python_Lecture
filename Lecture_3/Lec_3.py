# # Анонимные, lambda функции
# def mult(x):
#     return x**2

# def sum(x):
#     return x+10

# print(sum(mult(2)))

# sum = lambda x: x+10
# mult = lambda x: x**2
# print(sum(mult(2)))

# def mult2(x):
#     return x**3

# def sum1(x):
#     return x+22

# print(sum1(mult2(2)))


# def mult4(x):
#     return x**5


# def sum3(x):
#     return x+242


# print(sum3(mult2(2)))

# List comprehension  создаем списки


# Задача. составить список квадратов четных чисел из файла

# path = 'Lecture_3/file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []

# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)

# Упрощенный вариант

# def select(f, col):
#     return [f(x) for x in col] # формируем новый список и сразу же его возвращаем


# def where(f, col):
#     return [x for x in col if f(x)] # в качестве аргумента принимает функцию и некий набор данных


# data = '1 2 3 5 8 15 23 38'.split() # набор строк '1', '2', '3'... и т д
# # print(data)
# res = select(int, data) # преобразование строк в число
# # print(res)
# data = where(lambda e: not e % 2, res)
# # print(data)
# data = list(select(lambda e: (e, e**2), data))
# print(data)

# map

# li= [x for x in range(1,10)]
# li = list(map(lambda x: x+10, li))

# print(li)

# data = list(map(int, input().split())) # вводить значения с клавиатуры

# data = list(map(int, '1 2 5 8 6 55 '.split()))
# for e in data:
#     print(e*10, end= ' ')

# print('--') # если не указать тип данных list, то 2 раз не распечатает список
# for e in data:
#     print(e*10, end= ' ')

# в предыдущем примере избавились от функции select с помощью map

# def where(f, col):    # в качестве аргумента принимает функцию и некий набор данных
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()  # набор строк '1', '2', '3'... и т д
# res = map(int, data)  # преобразование строк в число
# data = where(lambda e: not e % 2, res)
# data = list(map(lambda e: (e, e**2), data))
# print(data)

# Функция filter()

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2, data))

# print(res)

# в предыдущем примере избавились от функции select с помощью map, затем от where с помощью filter

# data = '1 2 3 5 8 15 23 38'.split()  # набор строк '1', '2', '3'... и т д
# res = map(int, data)  # преобразование строк в число
# data = filter(lambda e: not e % 2, res)
# data = list(map(lambda e: (e, e**2), data))
# print(data)

# Функция zip()

# user = ['slnnvlk', 'sdnc', 'skvm', 'jdk']
# ids = [4, 5, 9, 12]
# salary = [111, 555, 633]

# data = list(zip(user, ids, salary))
# print(data)

# Функция enumerate()

user = ['slnnvlk', 'sdnc', 'skvm', 'jdk']

data = list(enumerate(user))
print(data)
