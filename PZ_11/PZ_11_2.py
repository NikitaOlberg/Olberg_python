# Из предложенного текстового файла (text18-17.txt) вывести на экран его содержимое,
# количество знаков препинания. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно поставив последнюю строку между первой и второй.

d = 0
for i in open('text18-17.txt', encoding='UTF-16'):
    print(i, end='')
    for j in i:
        if j == '.' or j == ':' or j == ',' or j == '!':
            d += 1
print(end='\n')
print('Количество знаков препинания: ', d, end='\n')

f1 = open('text18-17.txt', encoding='UTF-16')
lst = f1.readlines()

t = lst[-1]
i = len(lst)-1
while i > 1:
    lst[i] = lst[i-1]
    i -= 1
lst[1] = t + "\n"

f1.close()

f2 = open('text18-18.txt', 'w')
f2.writelines(lst)
f2.close()