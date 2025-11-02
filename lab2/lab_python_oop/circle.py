from lab_python_oop.shape import Figure
from lab_python_oop.shape_color import Color
import math


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, r_param):
        self.r = r_param
        self.fc = Color()
        self.fc.colorproperty = color_param

    def area(self):
        return math.pi*(self.r**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.fc.colorproperty,
            self.r,
            self.area()
        )
