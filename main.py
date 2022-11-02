from random import randint as r
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def GPA_calculation_s(self):
        Grades = []
        for item in list(self.grades.values()):
            Grades.extend(item)
        average_grade = sum(Grades) / len(Grades)
        return float(f'{average_grade :.2}')

    def grade_lr(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.GPA_calculation_s() :.2}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other.name} не студент')
            return
        return f'Оценка {self.name}({self.GPA_calculation_s()}) меньше оценки ' \
               f'{other.name}({other.GPA_calculation_s()})' if self.GPA_calculation_s() < \
                                                               other.GPA_calculation_s() else f'Оценка {self.name}({self.GPA_calculation_s()}) ' \
                                                                                              f'не меньше оценки {other.name}({other.GPA_calculation_s()})'

    def __gt__(self, other):
        if not isinstance(other, Student):
            print(f'{other.name} не студент')
            return
        return f'Оценка {self.name}({self.GPA_calculation_s()}) больше оценки ' \
               f'{other.name}({other.GPA_calculation_s()})' if self.GPA_calculation_s() > \
                                                               other.GPA_calculation_s() else f'Оценка {self.name}({self.GPA_calculation_s()}) ' \
                                                                                              f'не больше оценки {other.name}({other.GPA_calculation_s()})'

    def __eq__(self, other):
        if not isinstance(other, Student):
            print(f'{other.name} не студент')
            return
        return f'Оценка {self.name}({self.GPA_calculation_s()}) равна оценке ' \
               f'{other.name}({other.GPA_calculation_s()})' if self.GPA_calculation_s() == other.GPA_calculation_s() else f'Оценка {self.name}({self.GPA_calculation_s()}) не равна оценке ' \
               f'{other.name}({other.GPA_calculation_s()})'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.GPA_calculation_l() :.2}'

    def GPA_calculation_l(self):
        Grades = []
        for item in list(self.grades.values()):
            Grades.extend(item)
        average_grade = sum(Grades) / len(Grades)
        return float(f'{average_grade :.2}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other.name} не лектор')
            return
        return f'Оценка {self.name}({self.GPA_calculation_l()}) меньше оценки ' \
               f'{other.name}({other.GPA_calculation_l()})' if self.GPA_calculation_l() < \
                                                               other.GPA_calculation_l() else f'Оценка {self.name}({self.GPA_calculation_l()}) ' \
                                                                                              f'не меньше оценки {other.name}({other.GPA_calculation_l()})'

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other.name} не лектор')
            return
        return f'Оценка {self.name}({self.GPA_calculation_l()}) больше оценки ' \
               f'{other.name}({other.GPA_calculation_l()})' if self.GPA_calculation_l() > \
                                                               other.GPA_calculation_l() else f'Оценка {self.name}({self.GPA_calculation_l()}) ' \
                                                                                              f'не больше оценки {other.name}({other.GPA_calculation_l()})'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other.name} не лектор')
            return
        return f'Оценка {self.name}({self.GPA_calculation_l()}) равна оценке ' \
               f'{other.name}({other.GPA_calculation_l()})' if self.GPA_calculation_l() == other.GPA_calculation_l() else f'Оценка {self.name}({self.GPA_calculation_l()}) не равна оценке ' \
                                                                                                                          f'{other.name}({other.GPA_calculation_l()})'

class Reviewer(Mentor):

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


def average_students_grade(list_students, course):
    list_grades = list_students[0].grades[course] + list_students[1].grades[course]
    return f'Средняя оценка студентов за курс {course}: {sum(list_grades) / len(list_grades) :.2}'

def average_lecturers_grade(list_lecturers, course):
    list_grades = list_lecturers[0].grades[course] + list_lecturers[1].grades[course]
    return f'Средняя оценка лекторов за курс {course}: {sum(list_grades) / len(list_grades) :.2}'


lecturer_1 = Lecturer('Sam', 'Meet')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Shon', 'Woker')
lecturer_2.courses_attached += ['Git']
lecturer_2.courses_attached += ['Python']
####################################################################
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_1.grade_lr(lecturer_1, 'Python', r(1, 10))
student_1.grade_lr(lecturer_1, 'Python', r(1, 10))
student_1.grade_lr(lecturer_1, 'Git', r(1, 10))
student_1.grade_lr(lecturer_1, 'Git', r(1, 10))

student_1.grade_lr(lecturer_2, 'Python', r(1, 10))
student_1.grade_lr(lecturer_2, 'Python', r(1, 10))
student_1.grade_lr(lecturer_2, 'Git', r(1, 10))
student_1.grade_lr(lecturer_2, 'Git', r(1, 10))


student_2 = Student('Pol', 'Teember', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

student_2.grade_lr(lecturer_1, 'Python', r(1, 10))
student_2.grade_lr(lecturer_1, 'Python', r(1, 10))
student_2.grade_lr(lecturer_1, 'Git', r(1, 10))
student_2.grade_lr(lecturer_1, 'Git', r(1, 10))

student_2.grade_lr(lecturer_2, 'Python', r(1, 10))
student_2.grade_lr(lecturer_2, 'Python', r(1, 10))
student_2.grade_lr(lecturer_2, 'Git', r(1, 10))
student_2.grade_lr(lecturer_2, 'Git', r(1, 10))
####################################################################
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', r(1, 10))
reviewer_1.rate_hw(student_1, 'Python', r(1, 10))

reviewer_1.rate_hw(student_2, 'Python', r(1, 10))
reviewer_1.rate_hw(student_2, 'Python', r(1, 10))


reviewer_2 = Reviewer('Ann', 'Buddy')
reviewer_2.courses_attached += ['Git']

reviewer_2.rate_hw(student_1, 'Git', r(1, 10))
reviewer_2.rate_hw(student_1, 'Git', r(1, 10))

reviewer_2.rate_hw(student_2, 'Git', r(1, 10))
reviewer_2.rate_hw(student_2, 'Git', r(1, 10))
####################################################################

print('Студенты:')
print(student_1, student_2, sep='\n\n')
print()
print('Лекторы:')
print(lecturer_1, lecturer_2, sep='\n\n')
print()
print('Эксперты:')
print(reviewer_1, reviewer_2, sep='\n\n')
print('-' * 100)

print(student_1 < student_2)
print(student_2 > student_1)
print(student_1 == student_2)
print(student_1 == lecturer_2)
print()
print(lecturer_1 < lecturer_2)
print(lecturer_2 > lecturer_1)
print(lecturer_1 == lecturer_2)
print(lecturer_1 == student_2)
print('-' * 100)

print(average_students_grade([student_1, student_2], 'Python'))
print(average_students_grade([student_1, student_2], 'Git'))
print()
print(average_lecturers_grade([lecturer_1, lecturer_2], 'Python'))
print(average_lecturers_grade([lecturer_1, lecturer_2], 'Git'))