import unittest
import math
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

class TestArea(unittest.TestCase):

    def test_rectangle_area(self):
        rect = Rectangle("Синий", 2, 2)
        self.assertEqual(rect.area(), 4.0)

    def test_сircle_area(self):
        rect = Circle("Зеленый", 2)
        self.assertEqual(rect.area(), math.pi * 2 ** 2)

    def test_square_area(self):
        rect = Square("Красный", 2)
        self.assertEqual(rect.area(), 4.0)


if __name__ == '__main__':
    unittest.main()
