# Рефакторинг файла RK1.py
from operator import itemgetter


class Teacher:
    """Преподаватель"""
    def __init__(self, id, surname, salary, course_id):
        self.id = id
        self.surname = surname
        self.salary = salary
        self.course_id = course_id


class Course:
    """Учебный курс"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class TeacherCourse:
    """Преподаватели курсов"""
    def __init__(self, teacher_id, course_id):
        self.teacher_id = teacher_id
        self.course_id = course_id


def get_one_to_many(teachers, courses):
    """Соединение данных один-ко-многим"""
    return [(t.surname, t.salary, c.name)
            for c in courses
            for t in teachers
            if t.course_id == c.id]


def get_many_to_many(teachers, courses, teachers_courses):
    """Соединение данных многие-ко-многим"""
    many_to_many_temp = [(c.name, tc.course_id, tc.teacher_id)
                         for c in courses
                         for tc in teachers_courses
                         if c.id == tc.course_id]

    return [(t.surname, t.salary, course_name)
            for course_name, course_id, teacher_id in many_to_many_temp
            for t in teachers if t.id == teacher_id]


def task_a1(one_to_many):
    """Задание А1: отсортировать по названию курса"""
    return sorted(one_to_many, key=itemgetter(2))


def task_a2(one_to_many, courses):
    """Задание А2: суммарная зарплата преподавателей по курсам"""
    res_2_unsorted = []
    for c in courses:
        course_teachers = list(filter(lambda i: i[2] == c.name, one_to_many))
        if course_teachers:
            total_salary = sum([salary for _, salary, _ in course_teachers])
            res_2_unsorted.append((c.name, total_salary))

    return sorted(res_2_unsorted, key=itemgetter(1), reverse=True)


def task_a3(many_to_many, courses):
    """Задание А3: курсы со словом 'данных' и их преподаватели"""
    res_3 = {}
    for c in courses:
        if 'данных' in c.name:
            course_teachers = list(filter(lambda i: i[2] == c.name, many_to_many))
            teacher_surnames = [surname for surname, _, _ in course_teachers]
            res_3[c.name] = teacher_surnames
    return res_3


def main():
    """Основная функция с тестовыми данными"""
    # Тестовые данные
    courses = [
        Course(1, 'Математический анализ'),
        Course(2, 'Программирование на Python'),
        Course(3, 'Базы данных'),
        Course(4, 'Алгоритмы и структуры данных'),
        Course(5, 'Физика'),
    ]

    teachers = [
        Teacher(1, 'Иванов', 50000, 1),
        Teacher(2, 'Петров', 60000, 2),
        Teacher(3, 'Сидоров', 55000, 3),
        Teacher(4, 'Кузнецов', 65000, 4),
        Teacher(5, 'Попов', 52000, 5),
        Teacher(6, 'Смирнов', 58000, 1),
        Teacher(7, 'Федоров', 62000, 2),
    ]

    teachers_courses = [
        TeacherCourse(1, 1),
        TeacherCourse(1, 3),
        TeacherCourse(2, 2),
        TeacherCourse(3, 3),
        TeacherCourse(4, 4),
        TeacherCourse(5, 5),
        TeacherCourse(6, 1),
        TeacherCourse(7, 2),
        TeacherCourse(2, 4),
    ]

    # Получаем соединения данных
    one_to_many = get_one_to_many(teachers, courses)
    many_to_many = get_many_to_many(teachers, courses, teachers_courses)

    # Выполняем задания
    print('Задание А1')
    res_1 = task_a1(one_to_many)
    for surname, salary, course_name in res_1:
        print(f'Курс: {course_name}, Преподаватель: {surname}, Зарплата: {salary}')

    print('\nЗадание А2')
    res_2 = task_a2(one_to_many, courses)
    for course_name, total_salary in res_2:
        print(f'Курс: {course_name}, Суммарная зарплата: {total_salary}')

    print('\nЗадание А3')
    res_3 = task_a3(many_to_many, courses)
    for course_name, teachers_list in res_3.items():
        teachers_str = ', '.join(teachers_list) if teachers_list else 'нет преподавателей'
        print(f'Курс: {course_name}, Преподаватели: {teachers_str}')


if __name__ == "__main__":
    main()
