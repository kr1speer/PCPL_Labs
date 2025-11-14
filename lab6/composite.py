from abc import ABC, abstractmethod
from typing import List
from enum import Enum

class CarType(Enum):
    SEDAN = "sedan"
    SUV = "suv"
    SPORT = "sport"

class CarComponent(ABC):
    """Абстрактный компонент для паттерна Composite"""

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

class CarPart(CarComponent):
    """Автозапчасть (Leaf)"""

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def get_description(self) -> str:
        return f"Запчасть: {self.name} - {self.price} руб."

class Car(CarComponent):
    """Автомобиль (Leaf)"""

    def __init__(self, model: str, base_price: float, car_type: CarType):
        self.model = model
        self.base_price = base_price
        self.car_type = car_type
        self.options: List[CarPart] = []

    def add_option(self, option: CarPart):
        self.options.append(option)

    def get_price(self) -> float:
        options_price = sum(option.get_price() for option in self.options)
        return self.base_price + options_price

    def get_description(self) -> str:
        description = f"Автомобиль: {self.model} ({self.car_type.value}) - {self.base_price} руб."
        if self.options:
            description += "\n  Доп. опции:"
            for option in self.options:
                description += f"\n    - {option.get_description()}"
        return description

class CarPackage(CarComponent):
    """Пакет автомобилей (Composite)"""

    def __init__(self, name: str):
        self.name = name
        self.children: List[CarComponent] = []

    def add(self, component: CarComponent):
        self.children.append(component)

    def remove(self, component: CarComponent):
        self.children.remove(component)

    def get_price(self) -> float:
        return sum(child.get_price() for child in self.children)

    def get_description(self) -> str:
        description = f"Пакет: {self.name}\n"
        for child in self.children:
            child_desc = child.get_description()
            # Добавляем отступы для вложенных элементов
            for line in child_desc.split('\n'):
                description += f"  {line}\n"
        description += f"Общая стоимость пакета: {self.get_price()} руб."
        return description

# Фабрика для создания тестовых данных
def create_sample_autosalon():
    """Создание тестового автосалона"""
    # Создаем запчасти
    leather_seats = CarPart("Кожаные сиденья", 50000)
    navigation = CarPart("Навигационная система", 30000)
    sport_kit = CarPart("Спортивный обвес", 70000)

    # Создаем автомобили
    sedan = Car("Toyota Camry", 2500000, CarType.SEDAN)
    sedan.add_option(leather_seats)
    sedan.add_option(navigation)

    suv = Car("Honda CR-V", 3200000, CarType.SUV)
    suv.add_option(navigation)

    sport_car = Car("Porsche 911", 8500000, CarType.SPORT)
    sport_car.add_option(leather_seats)
    sport_car.add_option(sport_kit)

    # Создаем пакеты
    family_package = CarPackage("Семейный пакет")
    family_package.add(sedan)
    family_package.add(suv)

    premium_package = CarPackage("Премиум пакет")
    premium_package.add(sport_car)

    # Главный пакет автосалона
    autosalon = CarPackage("Автосалон 'Престиж'")
    autosalon.add(family_package)
    autosalon.add(premium_package)

    return autosalon
