# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Произведение элементов:
# Количество пар, для которых произведение элементов делится на 3
l = ['-99 6 12 -36 20 45 100 -15']
f3 = open('data_1.txt', 'w')
f3.writelines(l)
f3.close()

f4 = open('data_2.txt', 'w')
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()

f3 = open('data_1.txt')
lst = f3.read()
lst = lst.split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
f3.close()

t = 0
multiplication = []
for i in range(round(len(lst)/2)):
    if (t + 1) <= len(lst):
        multiplication.append(lst[t] * lst[t+1])
        t += 2
    elif (t + 1) > len(lst) and len(lst) % 2 != 0:
        multiplication.append(lst[t] * lst[t - 1])
    elif (t + 1) > len(lst) and len(lst) % 2 == 0:
        break

count = 0
for i in range(len(multiplication)):
    if multiplication[i]%3 == 0:
        count += 1

for i in range(len(multiplication)):
    multiplication[i] = str(multiplication[i])

string_multipl = " ".join(multiplication)

f4 = open('data_2.txt', 'a')
f4.write('\n')
print('Количество элементов:', len(lst), 'Количество пар, для которых произведение элементов делится на 3:', count, file=f4)
f4.write('Произведение элементов: ')
f4.writelines(string_multipl)
f4.close()