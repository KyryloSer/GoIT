import sqlite3
from datetime import datetime
import faker
from random import randint, choice

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_SUBJECTS = 5
NUMBER_TEACHERS = 3
NUMBER_MARKS = 20


def generate_fake_data(number_students, number_teachers) -> tuple():
    fake_groups = [312, 422, 535]  # здесь будем хранить группы
    fake_students = []  # здесь будем хранить студентов
    fake_subjects = ['PHP', 'Java', 'Python', 'C++', 'Go']  # здесь будем хранить предметы
    fake_teachers = []  # здесь будем хранить преподавателей
    fake_marks = [2, 3, 4, 5]  # здесь будем хранить оценки
    '''Возьмём три компании из faker и поместим их в нужную переменную'''
    fake_data = faker.Faker('en-US')

    # Создадим набор студентов в количестве number_students
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Сгенерируем теперь number_teachers количество преподавателей'''
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    return fake_students, fake_teachers, fake_groups, fake_marks, fake_subjects


def prepare_data(students, teachers, groups, marks, subjects) -> tuple():
    for_groups = []
    for_teachers = []
    for_subjects = []
    for_students = []
    for_marks = []
    # подготавливаем список кортежей названий компаний
    for group in groups:
        for_groups.append((group,))
    for teacher in teachers:
        for_teachers.append((teacher,))
    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))
    for student in students:
        for_students.append((student,randint(1, NUMBER_GROUPS)))
    for month in range(1, 10 + 1):
        # Выполняем цикл по месяцам'''
        m_date = datetime(2021, month, randint(1, 30)).date()
        for student_id in range(1, NUMBER_STUDENTS + 1):
            for i in range(1, 2 + 1):
                for_marks.append((student_id, randint(1,NUMBER_SUBJECTS), choice(marks),m_date))
    return for_students, for_teachers, for_groups, for_marks, for_subjects


def insert_data_to_db(students, teachers, groups, marks, subjects) -> None:
    # Создадим соединение с нашей БД и получим объект курсора для манипуляций с данными

    with sqlite3.connect('Script_students_sqlite.db') as con:

        cur = con.cursor()

        '''Заполняем таблицу groups. И создаем скрипт для вставки, где переменные, которые будем вставлять отметим
        знаком заполнителя (?) '''

        sql_to_groups = """INSERT INTO groups(name)
                               VALUES (?)"""

        '''Для вставки сразу всех данных воспользуемся методом executemany курсора. Первым параметром будет текст
        скрипта, а вторым данные (список кортежей).'''

        cur.executemany(sql_to_groups, groups)

        sql_to_teachers = """INSERT INTO teachers(name)
                                VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_students = """INSERT INTO students(name, group_id)
                                VALUES(?,?)"""
        cur.executemany(sql_to_students, students)

        sql_to_subjects = """INSERT INTO subjects(name, teacher_id)
                                VALUES(?,?)"""
        cur.executemany(sql_to_subjects, subjects)
        sql_to_marks = """INSERT INTO marks(student_id, subject_id, mark, created_at)
                                VALUES(?,?,?,?)"""
        cur.executemany(sql_to_marks, marks)
        con.commit()


if __name__ == '__main__':
    students, teachers, groups, marks, subjects = generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS)
    students, teachers, groups, marks, subjects = prepare_data(students, teachers, groups, marks, subjects)
    insert_data_to_db(students, teachers, groups, marks, subjects)
