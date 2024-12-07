# Дано целое положительное число. Проверить истинность высказывания: «Данное
# число является четным двузначным».
number = input("Введите целое положительное число: ")

while type(number) != int:
    try:
        number = int(number)
        if number < 0:
            print("Неправильно ввели!")
            number = input("Введите целое положительное число: ")

    except ValueError:
        print("Неправильно ввели!")
        number = input("Введите целое положительное число: ")

if 9 < number < 100 and number % 2 == 0:
    print('True')
else:
    print('False')