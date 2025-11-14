import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab_python_fp.field import field
from lab_python_fp.unique import Unique
from lab_python_fp.gen_random import gen_random

class TestLabFunctionsTDD(unittest.TestCase):

    def setUp(self):
        self.test_goods = [
            {'title': 'Ковер', 'price': 245, 'color': 'green'},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
            {'title': None, 'price': 1000},
            {'invalid': 'item'}
        ]

    def test_field_single_key(self):
        """Тест field с одним ключом"""
        result = list(field(self.test_goods, 'title'))
        expected = ['Ковер', 'Диван для отдыха']
        self.assertEqual(result, expected)

    def test_field_multiple_keys(self):
        """Тест field с несколькими ключами"""
        result = list(field(self.test_goods, 'title', 'price'))
        expected = [
            {'title': 'Ковер', 'price': 2000},
            {'title': 'Диван для отдыха', 'price': 5300},
            {'price': 1000}
        ]
        self.assertEqual(result, expected)

    def test_field_empty_list(self):
        """Тест field с пустым списком"""
        result = list(field([], 'title'))
        self.assertEqual(result, [])

    def test_unique_numbers(self):
        """Тест Unique с числами"""
        data = [1, 1, 2, 2, 3, 9, 1, 2, 3]
        result = list(Unique(data))
        expected = [1, 2, 3]
        self.assertEqual(result, expected)

    def test_unique_strings_case_sensitive(self):
        """Тест Unique с регистрозависимыми строками"""
        data = ['a', 'A', 'b', 'B', 'a', 'A']
        result = list(Unique(data))
        expected = ['a', 'A', 'b', 'B']
        self.assertEqual(result, expected)

    def test_unique_strings_case_insensitive(self):
        """Тест Unique с регистронезависимыми строками"""
        data = ['a', 'A', 'b', 'B', 'a', 'A']
        result = list(Unique(data, ignore_case=True))
        expected = ['a', 'b']
        self.assertEqual(result, expected)

    def test_gen_random_count(self):
        """Тест gen_random на количество элементов"""
        count = 5
        result = list(gen_random(count, 1, 10))
        self.assertEqual(len(result), count)

    def test_gen_random_range(self):
        """Тест gen_random на диапазон значений"""
        begin, end = 1, 5
        result = list(gen_random(10, begin, end))
        for num in result:
            self.assertTrue(begin <= num <= end)

if __name__ == '__main__':
    unittest.main()
