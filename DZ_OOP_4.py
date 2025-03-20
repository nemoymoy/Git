# Задание № 4. Полевые испытания.

from functools import total_ordering

class Mentor:
    def __init__(self, name, surname, courses_attached=None):
        if courses_attached is None:
            courses_attached = []
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached

# Создание класса Экспертов
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def add_courses_attached(self, courses_attached):
        self.courses_attached.append(courses_attached)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Создание класса Лекторов
@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        return(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: '
               f'{sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values()))}')

    def add_courses_attached(self, courses_attached):
        self.courses_attached.append(courses_attached)

    def __eq__(self, other):
        return (sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values())) ==
                sum(map(sum, other.grades.values())) / sum(map(len, other.grades.values())))

    def __lt__(self, other):
        return (sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values())) <
                sum(map(sum, other.grades.values())) / sum(map(len, other.grades.values())))

# Создание класса Студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached
        and grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: '
               f'{sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values()))}\nКурсы в процессе изучения: '
               f'{', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}')

    def __eq__(self, other):
        return (sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values())) ==
                sum(map(sum, other.grades.values())) / sum(map(len, other.grades.values())))

    def __lt__(self, other):
        return (sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values())) <
                sum(map(sum, other.grades.values())) / sum(map(len, other.grades.values())))

# Функция подсчета средней оценки по выбранному курсу у всех студентов по списку
def average_score_for_students(list_students, course = ''):
    if not isinstance(list_students, list):
        return print('Нет списка студентов')
    sum_all_students = 0
    len_all_score = 0
    for student in list_students:
        if course in student.grades.keys():
            sum_all_students += sum(student.grades[course])
            len_all_score += len(student.grades[course])
        else:
            print(f'Студент {student.surname} не изучает курс {course}!')
    return print(f'Средняя оценка всех студентов по курсу {course} = {sum_all_students / len_all_score}')

# Функция подсчета средней оценки по выбранному курсу у всех лекторов по списку
def average_score_for_lecturers(list_lecturers, course = ''):
    if not isinstance(list_lecturers, list):
        return print('Нет списка лекторов')
    sum_all_lecturers = 0
    len_all_score = 0
    for lecturer in list_lecturers:
        if course in lecturer.grades.keys():
            sum_all_lecturers += sum(lecturer.grades[course])
            len_all_score += len(lecturer.grades[course])
        else:
            print(f'Лектор {lecturer.surname} не преподает курс {course}!')
    return print(f'Средняя оценка всех лекторов по курсу {course} = {sum_all_lecturers / len_all_score}')

# Создаем экземпляры класса Экспертов
cool_reviewer = Reviewer('Some_R', 'Buddy_R')

cool_reviewer_new = Reviewer('Some_new_R', 'Buddy_new_R')

# Выводим информацию об Экспертах
print(f'Эксперт:\n{cool_reviewer}')

print(f'Эксперт:\n{cool_reviewer_new}')

# Добавляем курсы Экспертам
cool_reviewer.add_courses_attached('Python')
cool_reviewer.add_courses_attached('Git')
cool_reviewer.add_courses_attached('Java')

cool_reviewer.add_courses_attached('Python')
cool_reviewer.add_courses_attached('Git')
cool_reviewer.add_courses_attached('Java')

# Создаем экземпляры класса Студентов
best_student = Student('Ruoy', 'Eman', 'your_gender')

good_student = Student('Sergei', 'Paramzin', 'male')

# Добавляем курсы Студентам
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.add_courses('Введение в программирование')

good_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['Java']
good_student.add_courses('Введение в программирование')

# Выставляем оценки Студентам
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 9)

cool_reviewer.rate_hw(good_student, 'Python', 10)
cool_reviewer.rate_hw(good_student, 'Python', 10)
cool_reviewer.rate_hw(good_student, 'Java', 9)

# Создаем экземпляры класса Лекторов
cool_lecturer = Lecturer('Some_L', 'Buddy_L')

cool_lecturer_new = Lecturer('Some_new_L', 'Buddy_new_L')

# Добавляем курсы Лекторам
cool_lecturer.add_courses_attached('Python')
cool_lecturer.add_courses_attached('Java')
cool_lecturer.add_courses_attached('Git')

cool_lecturer_new.add_courses_attached('Python')
cool_lecturer_new.add_courses_attached('Java')

# Выставляем оценки Лекторам
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
good_student.rate_lecturer(cool_lecturer, 'Java', 9)
good_student.rate_lecturer(cool_lecturer, 'Java', 9)
good_student.rate_lecturer(cool_lecturer, 'Java', 9)
good_student.rate_lecturer(cool_lecturer, 'Java', 9)
good_student.rate_lecturer(cool_lecturer, 'Java', 9)
good_student.rate_lecturer(cool_lecturer, 'Java', 9)
good_student.rate_lecturer(cool_lecturer, 'Java', 9)
good_student.rate_lecturer(cool_lecturer, 'Java', 9)
good_student.rate_lecturer(cool_lecturer, 'Java', 9)

best_student.rate_lecturer(cool_lecturer_new, 'Python', 10)
good_student.rate_lecturer(cool_lecturer_new, 'Java', 10)

# Выводим информацию о Лекторах
print(f'Лектор:\n{cool_lecturer}')

print(f'Лектор:\n{cool_lecturer_new}')

# Сравниваем Лекторов
print('Оценки Лекторов равны?', cool_lecturer == cool_lecturer_new)
print(f'Оценка Лектора {cool_lecturer.surname} меньше, чем у Лектора {cool_lecturer_new.surname}?', cool_lecturer < cool_lecturer_new)
print(f'Оценка Лектора {cool_lecturer.surname} больше, чем у Лектора {cool_lecturer_new.surname}?', cool_lecturer > cool_lecturer_new)

# Выводим информацию о Студентах
print(f'Студент:\n{best_student}')

print(f'Студент:\n{good_student}')

# Сравниваем Студентов
print('Оценки Студентов равны?', best_student == good_student)
print(f'Оценка студента {best_student.surname} меньше, чем у студента {good_student.surname}?', best_student < good_student)
print(f'Оценка студента {best_student.surname} больше, чем у студента {good_student.surname}?', best_student > good_student)

# Вызываем функцию вычисления средней оценки по выбранному курсу для списка студентов
average_score_for_students([best_student, good_student], 'Python')

# Вызываем функцию вычисления средней оценки по выбранному курсу для списка лекторов
average_score_for_lecturers([cool_lecturer, cool_lecturer_new], 'Python')
