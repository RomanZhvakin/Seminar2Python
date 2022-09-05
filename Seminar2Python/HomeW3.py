# Реализуйте алгоритм перемешивания списка.
import random
def chisla(number: int) -> list:
    list = []
    for i in range(number+1):
        list.append(i)
    return list
def mixList(list: list) -> list:
    for i in range(0, len(list)):
        mixedList = random.randint(0, len(list)-1)
        list[i], list[mixedList] = list[mixedList], list[i]
    return list
num = int(input('Введите размерность создаваемого списка:\n '))
initial_list = chisla(num)
print(f'Созданный начальный список:\n{initial_list}')
mixed_list = mixList(initial_list)
print(f'Перемешанный список:\n{mixed_list}\n')