# Урок 4, задача 3.
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = list(map(int, input('Insert numbers: ').split()))
print(list(filter(lambda x: numbers.count(x) == 1, numbers)))
