# Дана строка, состоящая из русских слов, набранных заглавными буквами и
# разделенных пробелами (одним или несколькими). Вывести строку, содержащую
# эти же слова, разделенные одним пробелом и расположенные в алфавитном порядке.

words = 'Мандарин Апельсин  Помидор Огурец'
list = words.split()
t = 1
while t < len(list):
    i = t - 1
    tpm = list[i + 1]
    while i >= 0 and list[i + 1] < list[i]:
        list[i + 1] = list[i]
        list[i] = tpm
        i -= 1
    t += 1
readywords = ' '.join(list)
print(readywords)
