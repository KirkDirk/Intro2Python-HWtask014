# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from math import ceil

tempnum = num = int(input("Введите целое положительное число: "))
array = []
temp = 0
stringnum = ''
while (temp < ceil(num**0.5)):
    array.append(tempnum % 2)
    tempnum //= 2
    temp += 1
print(f'Число', num, 'в двоичном виде запишется как: ')
array.reverse()
for i in range(len(array)):
    stringnum += str(array[i])
print(int(stringnum))