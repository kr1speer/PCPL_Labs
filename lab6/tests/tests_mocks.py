import unittest
from unittest.mock import Mock
from composite import CarPackage, Car

class TestAutosalonMocks(unittest.TestCase):
    """Mock тесты для автосалона"""

    def test_package_with_mock_cars(self):
        """Тест пакета с mock автомобилями"""
        package = CarPackage("Тестовый пакет")

        # Создаем mock автомобили
        mock_car1 = Mock(spec=Car)
        mock_car1.get_price.return_value = 1000000

        mock_car2 = Mock(spec=Car)
        mock_car2.get_price.return_value = 2000000

        package.add(mock_car1)
        package.add(mock_car2)

        self.assertEqual(package.get_price(), 3000000)
        mock_car1.get_price.assert_called()
        mock_car2.get_price.assert_called()

    def test_nested_mock_packages(self):
        """Тест вложенных пакетов с mock"""
        mock_inner_package = Mock(spec=CarPackage)
        mock_inner_package.get_price.return_value = 2500000

        outer_package = CarPackage("Внешний пакет")
        outer_package.add(mock_inner_package)

        self.assertEqual(outer_package.get_price(), 2500000)
        mock_inner_package.get_price.assert_called()

if __name__ == '__main__':
    unittest.main()
