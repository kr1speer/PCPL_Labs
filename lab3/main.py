from lab_python_fp.field import test
from lab_python_fp.gen_random import print_gen
from lab_python_fp.unique import test_unique
from lab_python_fp.sort import dates_print
from lab_python_fp.print_result import print_test
from lab_python_fp.cm_timer import test_timer
from lab_python_fp.process_data import process


def main():
    tasks = [test, print_gen, test_unique, dates_print, print_test, test_timer, process]

    try:
        number = int(input('Выберите номер задания от 1 до 7: '))
        return tasks[number - 1]()
    except (IndexError, ValueError):
        print("Неверный номер задания")
        return


if __name__ == "__main__":
    main()
