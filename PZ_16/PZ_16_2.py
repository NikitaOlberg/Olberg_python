# Создание базового класса "Фигура" и его наследование для создания классов
# "Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
# такие как вычисление площади и периметра, а классы-наследники будут иметь
# специфичные методы и свойства.

class Figura(object):

    def area(self):
        pass

    def perimeter(self):
        pass


class square(Figura):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class rectangle(Figura):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class circle(Figura):
    def __init__(self, legth, radius):
        self.legth = legth
        self.radius = radius

    def area(self):
        return (self.legth * self.radius)/2

    def perimeter(self):
        return self.legth

    def diameter(self):
        return 2 * self.radius


MySquare = square(6)
print(MySquare.area())
print(MySquare.perimeter())
MyRec = rectangle(3, 5)
print(MyRec.area())
print(MyRec.perimeter())
MyCircle = circle(20, 4)
print(MyCircle.area())
print(MyCircle.perimeter())
print(MyCircle.radius)
