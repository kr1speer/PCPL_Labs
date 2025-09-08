import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    while True:
            try:
                if len(sys.argv) > index:
                    return float(sys.argv[index])
                else:
                    return float(input(prompt + "\n"))
            except ValueError:
                print("Ошибка: введите корректное число")
                return float(input(prompt + "\n"))
            except IndexError:
                print(prompt)





def get_roots(a, b, c):

    result = []

    if a == 0:
        if b == 0:
            if c == 0:
                return ['∞ решений']
            else:

                return []
        else:

            if -c / b >= 0:
                root = math.sqrt(-c / b)
                result.append(root)
                result.append(-root)
            return result


    D = b*b - 4*a*c
    X = -b / (2.0*a)

    if D == 0.0 and X >= 0:
        root = math.sqrt(X)
        result.append(root)
        result.append(-root)
    if D > 0.0:
        sqD = math.sqrt(D)
        Z1 = (-b + sqD) / (2.0*a)
        Z2 = (-b - sqD) / (2.0*a)
        if Z1 >= 0:
            root1 = math.sqrt(Z1)
            result.append(root1)
            result.append(-root1)
        if Z2 >= 0:
            root2 = math.sqrt(Z2)
            result.append(root2)
            result.append(-root2)
    return result


def main():

    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_roots(a,b,c)

    if len(roots) == 1 and type(roots[0]) == str:
        print(roots[0])
        return

    if len(roots) == 0:
        print("Нет корней")
    else:
        print(f"Найдено {len(roots)} корня:")
    for i in range(len(roots)):
        print(f"x{i+1} = {roots[i]}")


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
