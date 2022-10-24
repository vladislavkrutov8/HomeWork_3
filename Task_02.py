# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input('Введите размер списка: '))

def get_list_from_input(n):
    str_list = [''] * n
    for i in range(n):
        str_list[i] = input(f'Input row {i + 1}: ')

    return str_list

a = int(get_list_from_input(n))

print(type(a))

n = str(get_list_from_input(n))
def multiplication_list(n):
    sum = 0
    for i in range(len(n)/2 + 1):
        sum = n[i] * n[len(n) - i - 1]
    return sum
print(sum)



