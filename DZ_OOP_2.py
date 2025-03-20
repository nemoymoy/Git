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
# Задание № 2. Атрибуты и взаимодействие классов.

class Mentor:
    def __init__(self, name, surname, courses_attached=None):
        if courses_attached is None:
            courses_attached = []
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached

# Создание класса Лекторов

class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached=None):
        super().__init__(name, surname, courses_attached)
        if courses_attached is None:
            courses_attached = []
        self.grades = {}

# Создание класса Экспертов

class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached=None):
        super().__init__(name, surname, courses_attached)
        if courses_attached is None:
            courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

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
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached \
        and grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

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

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

good_student = Student('Sergei', 'Paramzin', 'male')
good_student.courses_in_progress += ['C++']

cool_lecturer = Lecturer('Some', 'Buddy', ['Python', 'C++'])

best_student.rate_lecturer(cool_lecturer, 'Python', 9)
good_student.rate_lecturer(cool_lecturer, 'C++', 10)
good_student.rate_lecturer(cool_lecturer, 'C++', 10)

print(cool_lecturer.grades)