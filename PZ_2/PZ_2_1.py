# Дано трехзначное число number. Вывести число, полученное при прочтении
# исходного числа справа налево.
number = input('Введите трёхзначное число: ')  # 567 - ввод числа

while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print("Неправильно ввели!")
    number = input("Введите целое трёхзначное число: ")

digit = number % 10 * 100  # 700 - получаем с правого конца числа цифру и умножаем на 100
digit = digit + number // 100  # 700 + 5 - прибавляем к полученному числу с левого конца исходного числа цифру
digit = digit + number % 100 // 10 * 10  # 705 + 60 - прибавляем середину исходного трёхзначного числа
print("Полученное число при прочтении исходного справа налево: ", digit)
