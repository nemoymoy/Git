# Код из "Домашнего задания: квиз по теме ООП".
# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#     def add_courses(self, course_name):
#         self.finished_courses.append(course_name)
from functools import total_ordering


# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.finished_courses += ['Git']
# best_student.courses_in_progress += ['Python']
# best_student.grades['Git'] = [10, 10, 10, 10, 10]
# best_student.grades['Python'] = [10, 10]
#
# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# print(cool_mentor.courses_attached)

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)

# Код для проверки Домашнее задание «ООП: наследование, инкапсуляция и полиморфизм».
# Задание № 3. Полиморфизм и магические методы.


class Mentor:
    def __init__(self, name, surname, courses_attached=None):
        if courses_attached is None:
            courses_attached = []
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached

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
                sum(map(sum, other.grades.values())) / sum(map(len, self.grades.values())))

    def __lt__(self, other):
        return (sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values())) <
                sum(map(sum, other.grades.values())) / sum(map(len, self.grades.values())))

# Создание класса Экспертов

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def add_courses_attached(self, courses_attached):
        self.courses_attached.append(courses_attached)

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
                sum(map(sum, other.grades.values())) / sum(map(len, self.grades.values())))

    def __lt__(self, other):
        return (sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values())) <
                sum(map(sum, other.grades.values())) / sum(map(len, self.grades.values())))

# Проверка переноса метода выставления оценок в класс "Reviewer"

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_reviever = Reviewer('Some', 'Buddy', 'Python')
#
# cool_reviever.rate_hw(best_student, 'Python', 10)
# cool_reviever.rate_hw(best_student, 'Python', 10)
# cool_reviever.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)

# Проверка метода выставления оценок Лекторам в классе "Student"

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# good_student = Student('Sergei', 'Paramzin', 'male')
# good_student.courses_in_progress += ['C++']
#
# cool_lecturer = Lecturer('Some', 'Buddy', ['Python', 'C++'])
#
# best_student.rate_lecturer(cool_lecturer, 'Python', 9)
# good_student.rate_lecturer(cool_lecturer, 'C++', 10)
#
# print(cool_lecturer.grades)

# Создаем экземпляр класса Экспертов
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.add_courses_attached('Python')
cool_reviewer.add_courses_attached('Git')
cool_reviewer.add_courses_attached('Java')

# Выводим информацию об Эксперте
print(f'Эксперт:\n{cool_reviewer}')

# Создаем экземпляры класса Студентов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.add_courses('Введение в программирование')

good_student = Student('Sergei', 'Paramzin', 'male')
good_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['Java']
good_student.add_courses('Введение в программирование')

# Создаем экземпляры класса Лекторов
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.add_courses_attached('Python')
cool_lecturer.add_courses_attached('Java')
cool_lecturer.add_courses_attached('Git')

cool_lecturer_new = Lecturer('Some_new', 'Buddy_new')
cool_lecturer_new.add_courses_attached('Python')
cool_lecturer_new.add_courses_attached('Java')

# Выставляем оценки Лекторам
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
good_student.rate_lecturer(cool_lecturer, 'Java', 10)
good_student.rate_lecturer(cool_lecturer, 'Java', 10)
good_student.rate_lecturer(cool_lecturer, 'Java', 10)
good_student.rate_lecturer(cool_lecturer, 'Java', 10)
good_student.rate_lecturer(cool_lecturer, 'Java', 10)
good_student.rate_lecturer(cool_lecturer, 'Java', 10)
good_student.rate_lecturer(cool_lecturer, 'Java', 10)
good_student.rate_lecturer(cool_lecturer, 'Java', 10)
good_student.rate_lecturer(cool_lecturer, 'Java', 10)

best_student.rate_lecturer(cool_lecturer_new, 'Python', 9)
good_student.rate_lecturer(cool_lecturer_new, 'Java', 10)

# Выводим информацию о Лекторах
print(f'Лектор:\n{cool_lecturer}')
print(f'Лектор:\n{cool_lecturer_new}')

# Сравниваем Лекторов
print('Оценки Лекторов равны?', cool_lecturer == cool_lecturer_new)
print(f'Оценка Лектора {cool_lecturer.surname} меньше, чем у Лектора {cool_lecturer_new.surname}?', cool_lecturer < cool_lecturer_new)
print(f'Оценка Лектора {cool_lecturer.surname} больше, чем у Лектора {cool_lecturer_new.surname}?', cool_lecturer > cool_lecturer_new)

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
cool_reviewer.rate_hw(good_student, 'Java', 9)

# Выводим информацию о Студентах
print(f'Студент:\n{best_student}')
print(f'Студент:\n{good_student}')

# Сравниваем Студентов
print('Оценки Студентов равны?', best_student == good_student)
print(f'Оценка студента {best_student.surname} меньше, чем у студента {good_student.surname}?', best_student < good_student)
print(f'Оценка студента {best_student.surname} больше, чем у студента {good_student.surname}?', best_student > good_student)