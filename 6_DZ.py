# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го 
# члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = int(input("Введите первый элемент арифметической прогрессии: "))
dif = int(input("Введите разность арифметической прогрессии: "))
count = int(input("Введите количество элементов арифметической прогрессии: "))
print("Вывод элементов арифметической прогрессии: ", end = "")
list3 = [(a1 + (i - 1) * dif) for i in range(1, count + 1)]
print(list3)



# Задача 32: Определить элементs массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 1
# 19
# Вывод: [1, 9, 13, 14, 19]


array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = 5
max = 15

print(list(map(lambda x:x[0],[i for i in enumerate(array) if i[1]>=min and i[1]<=max])))