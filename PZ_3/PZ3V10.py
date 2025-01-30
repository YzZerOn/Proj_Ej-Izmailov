"""Вариант 10.
Даны два целых числа: А, В. Проверить истинность высказывания: 
«Ровно одно из чисел А и В нечетное»."""
def intcheck(x):
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print('Неправильный ввод числа!')
            x = input('Повторите попытку: ')

A = intcheck(input("Введите целое число A"))
B = intcheck(input("Введите целое число B"))

if A+B % 2 != 0:
    print("Одно из чисел нечётное")
else:
    print("Оба числа чётные/нечётные")
