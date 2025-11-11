import json
import sys
import random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.field import field
from lab_python_fp.cm_timer import cm_timer_1


path = sys.argv[1] if len(sys.argv) > 1 else 'data_light.json'

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    # Сортируем список профессий без повторений, игнорируя регистр
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=str.lower)

@print_result
def f2(arg):
    # Фильтруем только профессии программистов
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    # Добавляем "с опытом Python" к каждой профессии
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    # Генерируем зарплаты и объединяем с профессиями
    salaries = [f"зарплата {random.randint(100000, 200000)} руб." for _ in arg]
    return list(zip(arg, salaries))

def process():
    with cm_timer_1():
        f4(f3(f2(f1(data))))
