# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def make_list(x: int):
    my_list = []
    for _ in range(x):
        my_list.append(int(input('Введите число: ')))
    return my_list


def index_list(num_lst: list, start: int, end: int):
    indexes_list = []
    for i in range(len(num_lst)):
        if start <= num_lst[i] <= end:
            indexes_list.append(i)
    return indexes_list

list_size = make_list(int(input('Введите размер массива: ')))
minimum_range = int(input('Введите минимум диапазона: '))
maximum_range = int(input('Введите максимум диапазона: '))

print(*list_size)
print(*index_list(list_size, minimum_range, maximum_range))