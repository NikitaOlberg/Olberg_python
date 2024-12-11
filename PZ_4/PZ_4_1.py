# Дано целое число N (>0). Используя один цикл, найти сумму 1 + 1/(1!) + 1/(2!) +
# 1/(3!) + ... + 1/(N!) (выражение N! — N-факториал — обозначает произведение всех
# целых чисел от 1 до N: N! = 1-2-.. . N). Полученное число является приближенным
# значением константы e = exp(1).


digit = input("Введите целое число: ")
while type(digit) != int: # обработка исключений
 try:
     digit = int(digit)
 except ValueError:
     print("Неправильно ввели!")
     digit = input("Введите число: ")

sum = 1
division = 1
sup = digit
while digit:
    division = division * (sup - digit + 1)
    sum = sum + 1/division
    digit -= 1
print(sum)