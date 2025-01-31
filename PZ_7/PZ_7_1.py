# Дана строка. Преобразовать в ней все строчные буквы (как латинские, так и русские)
# в прописные.

letters = str(input('Введите строчные буквы: '))
while len(letters) <= 0:
    try:
        a = 1 / len(letters)
    except:
        print("Вы неправильно ввели")
        letters = str(input('Введите строчные буквы: '))
print(letters.upper())
