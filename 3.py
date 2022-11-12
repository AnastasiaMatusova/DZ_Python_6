# Задача №1 к 5 семинару
#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# txt = input ("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = 'абв'
# lst= [i for i in txt.split() if find_txt not in i ]
# print(f'Измененный текст: {" ".join(lst)}')

#улучшеный код
txt = input ("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
lst  = list(filter(lambda x: x != 'абв', txt.split()))
print(lst)