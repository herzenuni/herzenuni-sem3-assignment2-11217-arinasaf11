#Сафиуллина Арина ИВТ 2 курс
# Напишите программу, которая реализует нахождение наибольшего общего делителя двух чисел A, B.Тесты оформите с помощью pytest или UnitTest.
def nod(x, y):
    while y:
        x, y = y, x % y
    return x
a = int(input('a = '))
b = int(input('b = '))
print ('NOD = ', nod(a, b))
