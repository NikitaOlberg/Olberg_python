# Дана строка, состоящая из русских слов, набранных заглавными буквами и
# разделенных пробелами (одним или несколькими). Вывести строку, содержащую
# эти же слова, разделенные одним пробелом и расположенные в алфавитном порядке.
letters = str(input('Введите русские слова разделённые пробелом: '))
# words = 'Мандарин Апельсин  Помидор Огурец'
while len(letters) <= 0:
    try:
        a = 1 / len(letters)
    except:
        print("Вы неправильно ввели")
        letters = str(input('Введите русские слова разделённые пробелом: '))

list1 = letters.split()
for i in range(len(list1)):
    list1[i] = list1[i].capitalize()

# list1 = words.split()
t = 1
while t < len(list1):
    i = t - 1
    tpm = list1[i + 1]
    while i >= 0 and list1[i + 1] < list1[i]:
        list1[i + 1] = list1[i]
        list1[i] = tpm
        i -= 1
    t += 1
readywords = ' '.join(list1)
print(readywords)
