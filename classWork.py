import math


class Shape(object):
    def __init__(self, *sides):
        sides_qty = len(sides)

        if (sides_qty < 1) and (sides_qty > 4):
            raise ValueError('Ошибка. Вы ввели {} сторон, а должно быть от 1 до 4.'.format(sides_qty))
        else:
            if sides_qty == 1:
                self.sides = [n for n in sides] * 4
            elif sides_qty == 2:
                self.sides = [n for n in sides] * 2
            else:
                self.sides = [n for n in sides]

    def _calc_per(self):
        return sum(self.sides)

    def print_sides(self):
        print('Стороны фигуры : {}'.format(self.sides))

    def print_per(self):
        print('Периметр фигуры равен {}'.format(self._calc_per()))


class Rectangle(Shape):

    def _calc_sqr(self):
        return self.sides[0] * self.sides[1]

    def print_sqr(self):
        print("Площадь прямоугольника равна {}".format(self._calc_sqr()))


class Square(Rectangle):

    def print_sqr(self):
        print('Площадь квадрата равна {}'.format(self._calc_sqr()))


class Triangle(Shape):

    def __init__(self, *sides):

        sides_qty = len(sides)

        if sides_qty != 3:
            raise ValueError('Ошибка при инициализации треугольника! '
                             'Кол-во сторон {}, а должно быть 3.'.format(sides_qty))
        else:
            self.sides = [n for n in sides]

        self.sides.sort()

        larger_side = self.sides[len(self.sides) - 1]
        two_sides_sum = self.sides[0] + self.sides[1]

        if two_sides_sum <= larger_side:
            raise ValueError('Ошибка при инициализации треугольника! Со сторонами такой длины'
                             ' сторон построить треугольник невозможно!')

    def _calc_sqr(self):
        half_per = self._calc_per() / 2
        return math.sqrt(half_per * (half_per - self.sides[0]) *
                         (half_per - self.sides[1]) * (half_per - self.sides[2]))

    def print_sqr(self):
        print('Площадь треугольника равна {}'.format(self._calc_sqr()))


class Polygon(Shape):

    def __init__(self, *sides):

        sides_qty = len(sides)

        if sides_qty != 4:
            raise ValueError('Ошибка при инициализации четырехугольника!'
                             ' Кол-во сторон {}, а должно быть 4.'.format(sides_qty))
        else:
            self.sides = [n for n in sides]

        self.sides.sort()

        larger_side = self.sides[len(self.sides) - 1]
        three_sides_sum = self.sides[0] + self.sides[1] + self.sides[2]

        if three_sides_sum <= larger_side:
            raise ValueError('Ошибка при инициализации четырехугольника! '
                             'Со сторонами такой длины сторон построить четырехугольник невозможно!')

    def _calc_sqr(self):
        return 'Рассчитать площадь произвольного многоугольника без знания 2 углов невозможно!'

    def print_sqr(self):
        print(self._calc_sqr())


rect = Rectangle(int(input('Введите сторону A: ')), int(input('Введите сторону B: ')))
rect.print_sides()
rect.print_per()
rect.print_sqr()
print('\n')
sqr = Square(int(input('Введите сторону квадрата: ')))
sqr.print_sides()
sqr.print_per()
sqr.print_sqr()
print('\n')
tng = Triangle(int(input('Введите сторону A: ')), int(input('Введите сторону B: ')), int(input('Введите сторону C: ')))
tng.print_sides()
tng.print_per()
tng.print_sqr()
print('\n')
poly = Polygon(int(input('Введите сторону A: ')), int(input('Введите сторону B: ')),
               int(input('Введите сторону C: ')), int(input('Введите сторону D: ')))
poly.print_sides()
poly.print_per()
poly.print_sqr()
