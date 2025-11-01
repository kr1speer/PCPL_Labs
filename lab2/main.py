from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

from colorama import Fore
def main():
    # Параметры фигур (2 вариант, N = 2)
    N = 2

    # Создание фигур
    rectangle = Rectangle("белого", N, N)
    circle = Circle("синего", N)
    square = Square("красного", N)

    # Вывод информации о фигурах
    print(Fore.WHITE + str(rectangle))
    print(Fore.BLUE + str(circle))
    print(Fore.RED + str(square))


if __name__ == "__main__":
    main()
