'''Вариант 10. Даны целые положительные числа А и В (А > В). На отрезке длины А размещено максимально возможное количество отрезков длины В (без наложений). Используя операцию взятия остатка от деления нацело, найти длину незанятой части отрезка А.'''
def intcheck(x):
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Неправильный ввод числа!')
            x = input('Повторите попытку: ')
a = input('Введите число A: ')
a = intcheck(a)
b = input('Введите число B: ')
b = intcheck(b)
if a>b and a>0 and b>0:
    print(a % b)
else:
    print('A не должно быть меньше чем B или числа должны быть положительными')
