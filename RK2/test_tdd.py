# Рефакторинг файла RK1.py
import unittest
from RK2 import Teacher, Course, TeacherCourse, get_one_to_many, get_many_to_many, task_a1, task_a2, task_a3


class TestRK1(unittest.TestCase):

    def setUp(self):
        """Инициализация тестовых данных перед каждым тестом"""
        self.courses = [
            Course(1, 'Математический анализ'),
            Course(2, 'Программирование на Python'),
            Course(3, 'Базы данных'),
            Course(4, 'Алгоритмы и структуры данных'),
            Course(5, 'Физика'),
        ]

        self.teachers = [
            Teacher(1, 'Иванов', 50000, 1),
            Teacher(2, 'Петров', 60000, 2),
            Teacher(3, 'Сидоров', 55000, 3),
            Teacher(4, 'Кузнецов', 65000, 4),
            Teacher(5, 'Попов', 52000, 5),
            Teacher(6, 'Смирнов', 58000, 1),
            Teacher(7, 'Федоров', 62000, 2),
        ]

        self.teachers_courses = [
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

        self.one_to_many = get_one_to_many(self.teachers, self.courses)
        self.many_to_many = get_many_to_many(self.teachers, self.courses, self.teachers_courses)

    def test_task_a1(self):
        """
        Тест задания А1:
        Проверяем сортировку связей один-ко-многим по названию курса.
        """
        result = task_a1(self.one_to_many)

        # Проверяем, что результат отсортирован по названию курса (по алфавиту)
        self.assertEqual(result[0][2], 'Алгоритмы и структуры данных')
        self.assertEqual(result[1][2], 'Базы данных')
        self.assertEqual(result[2][2], 'Математический анализ')

        # Проверяем, что сортировка действительно работает
        course_names = [item[2] for item in result]
        self.assertEqual(course_names, sorted(course_names))

    def test_task_a2(self):
        """
        Тест задания А2:
        Проверяем подсчет суммарной зарплаты преподавателей по курсам
        и сортировку по убыванию суммы.
        """
        result = task_a2(self.one_to_many, self.courses)

        # Проверяем, что результат отсортирован по убыванию суммарной зарплаты
        salaries = [item[1] for item in result]
        self.assertEqual(salaries, sorted(salaries, reverse=True))
        # Создаем словарь для удобства проверки
        result_dict = {course: salary for course, salary in result}
        # Проверяем суммарную зарплату для курса "Программирование на Python"
        self.assertEqual(result_dict.get('Программирование на Python'), 122000)
        # Проверяем суммарную зарплату для курса "Математический анализ"
        self.assertEqual(result_dict.get('Математический анализ'), 108000)
        # Проверяем суммарную зарплату для курса "Алгоритмы и структуры данных"
        self.assertEqual(result_dict.get('Алгоритмы и структуры данных'), 65000)

    def test_task_a3(self):
        """
        Тест задания А3:
        Проверяем фильтрацию курсов по ключевому слову 'данных'
        и вывод списка преподавателей для этих курсов.
        """
        result = task_a3(self.many_to_many, self.courses)

        self.assertIn('Базы данных', result)
        self.assertIn('Алгоритмы и структуры данных', result)

        # Курсы без слова 'данных' не должны присутствовать
        self.assertNotIn('Математический анализ', result)
        self.assertNotIn('Программирование на Python', result)
        self.assertNotIn('Физика', result)

        # Проверяем преподавателей для курса 'Базы данных'
        # Из данных: Иванов (id=1) и Сидоров (id=3) ведут Базы данных
        teachers_for_db = result.get('Базы данных', [])
        self.assertIn('Иванов', teachers_for_db)
        self.assertIn('Сидоров', teachers_for_db)
        self.assertEqual(len(teachers_for_db), 2)

        # Проверяем преподавателей для курса 'Алгоритмы и структуры данных'
        # Из данных: Кузнецов (id=4) ведет Алгоритмы, Петров (id=2) тоже ведет Алгоритмы
        teachers_for_algo = result.get('Алгоритмы и структуры данных', [])
        self.assertIn('Кузнецов', teachers_for_algo)
        self.assertIn('Петров', teachers_for_algo)
        self.assertEqual(len(teachers_for_algo), 2)

if __name__ == '__main__':
    unittest.main()
