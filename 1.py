# Задача №3 к 2 семинару:
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# (1+1/n)^n

# count = 0
# multiply = 0
# number = int(input('Введите число: '))
# dictionary_ = {}
# while count < number:
#     for i in range(1, number+1):
#         dictionary_[i] = (1+(1/i))**i
#         count += 1
# round_ = 2
# for elem in dictionary_:
#     dictionary_[elem] = round(dictionary_[elem], 2)
# print(dictionary_)
# print(f'Сумма чисел в словаре:', sum(dictionary_.values()))

#улучшеный код
number = int(input('Введите число: ')) 
def sequence(number):
    return[round((1 + 1 / x)**x, 2) for x in range (1, number + 1)]   
print(f"Список из n чисел последовательности:" , sequence(number))
print(f"Сумма чисел в словаре:", round(sum(sequence(number))))