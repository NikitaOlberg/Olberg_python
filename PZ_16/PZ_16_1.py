# Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
# Добавьте методы для сложения, вычитания и умножения матриц.
import random


class Matrix:

    def __init__(self, rows=None, cols=None, data=None):
        if data is not None:
            self.data = data
            self.rows = len(data)
            self.cols = len(data[0]) if data else 0
        else:
            if rows is None or cols is None:
                print("Необходимо указать либо data, либо rows и cols")
            self.rows = rows
            self.cols = cols
            self.data = [[random.randint(0, 10) for j in range(cols)] for i in range(rows)]

    def prnt(self):
        for row in self.data:
            print(row)

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Матрицы должны быть одинакового размера для сложения")
        else:
            result = [[self.data[i][j] + other.data[i][j]for j in range(self.cols)]for i in range(self.rows)]
            for row in result:
                print(row)

    def sub(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Матрицы должны быть одинакового размера для вычитания")
        else:
            result = [[self.data[i][j] - other.data[i][j]for j in range(self.cols)]for i in range(self.rows)]
            for row in result:
                print(row)

    def mul(self, other):
        if self.cols != other.rows:
            print("Число столбцов первой матрицы должно быть равно числу строк второй матрицы")
        else:
            result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))for j in range(other.cols)]for i in range(self.rows)]
            for row in result:
                print(row)


matrix1 = Matrix(4, 4)
matrix2 = Matrix(4, 4)
matrix1.prnt()
print("Вывод 2 матрица: ")
matrix2.prnt()
print("Сложение: ")
matrix1.add(matrix2)
print("Вычитание: ")
matrix1.sub(matrix2)
print("Умножение: ")
matrix1.mul(matrix2)
