# Задача №3 к 3 семинару:
#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#улучшеный код
lst = list(map(float, input("Введите вещественные числа через пробел:\n").split()))
new_lst = [round(i % 1,2) for i in lst if i%1 != 0]
print(f'Разница между максимальным {max(new_lst)} и минимальным {min(new_lst)} значением дробной части элементов равна ' , max(new_lst) - min(new_lst))