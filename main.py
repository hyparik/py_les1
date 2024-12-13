from array import *
import time
import math

#Задание 1
print('Задание 1')
arr = [1, 1, 2, 3, 5, 8, 10, 12, 34, 38, 40, 41, 46, 50, 55, 89]
print(arr)
for i in range(len(arr)):
    if i < 15:
        print(i)

#Задание 2
print('Задание 2')
print('Введите число: ')
num = int(input())
if num > 0:
    print('Положительное')
elif num < 0:
    print('отрицательное')
else:
    print('Равно нулю')

#Задание 3
print('Задание 3')
def summa(first, second):
    return first + second
def sub(first, second):
    return first - second
def mult(first, second):
    return first * second
def div(first, second):
    return first / second
print('Первое число: ')
num1 = float(input())
print('Введите арифмитический оператор: ')
ao = input()
if (ao != '+' and ao != '-' and ao != '*' and ao !='/'):
    print('Error')
    exit()
print('Второе число: ')
num2 = float(input())
if ao == '+':
    print(f"{num1} + {num2} = {summa(num1, num2)}")
elif ao == '-':
    print(f"{num1} - {num2} = {sub(num1, num2)}")
elif ao == '*':
    print(f"{num1} * {num2} = {mult(num1, num2)}")
elif ao == '/':
    print(f"{num1} + {num2} = {div(num1, num2)}")

#Задание 4
print('Задание 4')
for i in range(10, 0, -1):
    time.sleep(1)
    print(i)

#Задание 5
print('Задание 5')
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print(f"D = {discr}")

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f"x1 = {x1} \nx2 = {x2}")
elif discr == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    print("Корней нет")



