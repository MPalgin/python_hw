from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):

        courses = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
                f'{self.average_mark()}\n'f'Курсы в процессе изучения: {courses}\n'
                f'Завершенные курсы: {finished_courses}')

    def __eq__(self, other):
        return self.average_mark() == other.average_mark()

    def __lt__(self, other):
        return self.average_mark() < other.average_mark()

    def __le__(self, other):
        return self.average_mark() <= other.average_mark()

    def __gt__(self, other):
        return self.average_mark() > other.average_mark()

    def __ge__(self, other):
        return self.average_mark() >= other.average_mark()

    def average_mark(self):
        marks_list = []
        for (key, values) in self.grades.items():
            for value in values:
                marks_list.append(value)
        return mean(marks_list)

    def rate_mentor(self, lecturer, course_name, lector_mark):
        if isinstance(lecturer, Lecturer):
            if course_name in self.courses_in_progress and course_name in lecturer.courses_attached:
                if course_name in lecturer.course_mark:
                    lecturer.course_mark[course_name] += [lector_mark]
                else:
                    lecturer.course_mark[course_name] = [lector_mark]
            else:
                return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_mark = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_mark()}'

    def __eq__(self, other):
        return self.average_mark() == other.average_mark()

    def __lt__(self, other):
        return self.average_mark() < other.average_mark()

    def __le__(self, other):
        return self.average_mark() <= other.average_mark()

    def __gt__(self, other):
        return self.average_mark() > other.average_mark()

    def __ge__(self, other):
        return self.average_mark() >= other.average_mark()

    def average_mark(self):
        marks_list = []
        for (key, values) in self.course_mark.items():
            for value in values:
                marks_list.append(value)
        return mean(marks_list)


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Petr', 'Random', 'secret')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.courses_in_progress += ['Excel']
best_student.finished_courses += ['Введение в программирование']

best_student_2 = Student('Liza', 'Nerandom', 'secret')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Java']
best_student_2.courses_in_progress += ['Excel']


cool_mentor = Reviewer('Yuriy', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']
cool_mentor.courses_attached += ['Excel']

cool_mentor_2 = Reviewer('Alex', 'Newbuddy')
cool_mentor_2.courses_attached += ['Python']
cool_mentor_2.courses_attached += ['Java']
cool_mentor_2.courses_attached += ['Excel']


cool_mentor.rate_hw(best_student, 'Python', 1)
cool_mentor.rate_hw(best_student, 'Java', 2)
cool_mentor.rate_hw(best_student, 'Excel', 3)

cool_mentor.rate_hw(best_student_2, 'Python', 4)
cool_mentor.rate_hw(best_student_2, 'Java', 5)
cool_mentor.rate_hw(best_student_2, 'Excel', 4)

cool_mentor_2.rate_hw(best_student, 'Python', 7)
cool_mentor_2.rate_hw(best_student, 'Java', 7)
cool_mentor_2.rate_hw(best_student, 'Excel', 8)

cool_mentor_2.rate_hw(best_student_2, 'Python', 10)
cool_mentor_2.rate_hw(best_student_2, 'Java', 4)
cool_mentor_2.rate_hw(best_student_2, 'Excel', 9)


lecturer_1 = Lecturer('Yuriy', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['Excel']

lecturer_2 = Lecturer('Alex', 'Newbuddy')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Java']
lecturer_2.courses_attached += ['Excel']

best_student.rate_mentor(lecturer_1, 'Python', 0)
best_student.rate_mentor(lecturer_1, 'Java', 0)
best_student.rate_mentor(lecturer_1, 'Excel', 0)

best_student.rate_mentor(lecturer_2, 'Python', 10)
best_student.rate_mentor(lecturer_2, 'Java', 2)
best_student.rate_mentor(lecturer_2, 'Excel', 4)

best_student_2.rate_mentor(lecturer_1, 'Python', 0)
best_student_2.rate_mentor(lecturer_1, 'Java', 0)
best_student_2.rate_mentor(lecturer_1, 'Excel', 0)

best_student_2.rate_mentor(lecturer_2, 'Python', 10)
best_student_2.rate_mentor(lecturer_2, 'Java', 2)
best_student_2.rate_mentor(lecturer_2, 'Excel', 4)

print(best_student)
print(best_student_2)

print(best_student_2 == best_student)
print(best_student_2 > best_student)
print(best_student_2 < best_student)
print(best_student_2 == best_student)
print(best_student_2 > best_student)
print(best_student_2 >= best_student)

print(lecturer_1)
print(lecturer_2)

print(lecturer_1 == lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 == lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 >= lecturer_2)


def avarege_course_mark(students_list, course_name):
    marks = []
    for student in students_list:
        for (key, values) in student.grades.items():
            if key == course_name:
                for value in values:
                    marks.append(value)

    return mean(marks)


def avarege_lectures_mark(lecturer_list, lecture_name):
    marks = []
    for lecturer in lecturer_list:
        for (key, values) in lecturer.course_mark.items():
            if key == lecture_name:
                for value in values:
                    marks.append(value)

    return mean(marks)


print(f'Средняя оценка студентов {avarege_course_mark([best_student, best_student_2], "Python")}')
print(f'Средняя оценка лекторов {avarege_lectures_mark([lecturer_1, lecturer_2], "Python")}')
