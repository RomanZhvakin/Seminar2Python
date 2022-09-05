# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
def sequence(number: float) -> list:
    tmp_list = []
    for i in range(1, number+1):
        tmp_list.append((1 + 1 / i) ** i)
    return tmp_list
def sumFloatsInList(list: list) -> float:
    sum = 0
    for i in list:
        sum += i
    return sum
num = int(input('Введите N: '))
list = sequence(num)
sum = sumFloatsInList(list)
print(f'\nПоследовательность для заданного N: {list}')
print(f'\nСумма элементов последовательности равна {sum}')