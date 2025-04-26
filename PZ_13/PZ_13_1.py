# Сгенерировать матрицу на произвольное количество элементов, в которой задается
# преобразование от предыдущего элемента к следующему на произвольное значение.

import random
rows, cols = random.randint(2,6), random.randint(2,6)
k = 0
random_matrix = [[k := k + random.randint(10,100) for j in range(cols)] for i in range(rows)]
print(random_matrix)

# В матрице найти сумму элементов первых двух строк.
summa = 0
for i in range(2):
    summa += sum(random_matrix[i])
print(summa)

