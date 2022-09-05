# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     *Пример:*
#     - 6782 -> 23
#     - 0,56 -> 11
def count(number: float) -> int:
    sum = 0
    string = str(number)
    for num in string:
        if num != '.':
            sum += int(num)
    return sum
num = float(input('\nВведите число: '))
print(f'\nСумма цифр введенного числа равна {count(num)}\n')