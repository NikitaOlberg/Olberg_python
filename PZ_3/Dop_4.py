# Дано целое число. Если оно является положительным, то прибавить к нему 20, в
# противном случае вычесть из него 5.

number = input('Введите целое число: ')  # 567 - ввод числа

while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print("Неправильно ввели!")
        number = input("Введите целое целое число: ")

if number > 0:
    number += 20
else:
    number -= 5
print(number)