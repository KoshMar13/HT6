# Урок 5, задача 1
#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

inp = list(map(str, input('Insert text: ').split()))
sample = input('Insert removing text: ')
print(list(filter(lambda x: x != sample, inp)))
