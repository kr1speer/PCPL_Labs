import unittest
from composite import CarPart, Car, CarPackage, CarType

class TestAutosalonTDD(unittest.TestCase):
    """TDD тесты для автосалона"""

    def test_car_part_creation(self):
        """Тест создания автозапчасти"""
        part = CarPart("Тормозные колодки", 8000)
        self.assertEqual(part.get_price(), 8000)
        self.assertIn("Тормозные колодки", part.get_description())

    def test_car_creation(self):
        """Тест создания автомобиля"""
        car = Car("Toyota Camry", 2500000, CarType.SEDAN)
        self.assertEqual(car.base_price, 2500000)
        self.assertEqual(car.car_type, CarType.SEDAN)
        self.assertEqual(car.get_price(), 2500000)  # Без опций

    def test_car_with_options(self):
        """Тест автомобиля с опциями"""
        car = Car("Honda Civic", 2000000, CarType.SEDAN)
        option1 = CarPart("Климат-контроль", 40000)
        option2 = CarPart("Кожаный салон", 80000)

        car.add_option(option1)
        car.add_option(option2)

        self.assertEqual(car.get_price(), 2120000)  # 2000000 + 40000 + 80000
        self.assertEqual(len(car.options), 2)

    def test_empty_package(self):
        """Тест пустого пакета"""
        package = CarPackage("Пустой пакет")
        self.assertEqual(package.get_price(), 0)
        self.assertEqual(len(package.children), 0)

    def test_package_with_cars(self):
        """Тест пакета с автомобилями"""
        package = CarPackage("Тестовый пакет")
        car1 = Car("Car1", 1000000, CarType.SEDAN)
        car2 = Car("Car2", 2000000, CarType.SUV)

        package.add(car1)
        package.add(car2)

        self.assertEqual(package.get_price(), 3000000)
        self.assertEqual(len(package.children), 2)

    def test_nested_packages(self):
        """Тест вложенных пакетов"""
        inner_package = CarPackage("Внутренний пакет")
        inner_package.add(Car("Small Car", 1500000, CarType.SEDAN))

        outer_package = CarPackage("Внешний пакет")
        outer_package.add(inner_package)
        outer_package.add(Car("Big Car", 3000000, CarType.SUV))

        self.assertEqual(outer_package.get_price(), 4500000)

if __name__ == '__main__':
    unittest.main()
