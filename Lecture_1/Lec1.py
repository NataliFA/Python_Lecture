# print('hello, world')

print('Введите а')
a = int(input())
print('Введите b')
b = int(input())
c = a + b
print(a, ' + ', b, ' = ', c) 

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return