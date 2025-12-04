from datetime import datetime, date
import statistics
from abc import ABC, abstractmethod


class Person():
    def __init__(self, firstname, lastname, personal_id_nr, date_of_birth):
        self.firstname = firstname
        self.lastname = lastname
        self.personal_id_nr = personal_id_nr
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

    def __repr__(self):
        return (f"Name: {self.fullname}\n"
                f"Age: {self.age}\n")


class Student(Person):
    def __init__(self, firstname, lastname, personal_id_nr, date_of_birth, class_name):
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth)
        self.class_name = class_name
        self.grades = {}  # {subject: [subject_grades]}

    def add_grade(self, subject, grade):
        if 1 <= grade <= 5:
            if subject not in self.grades.keys():
                self.grades[subject] = []
            self.grades[subject].append(grade)
            print(f"{self.firstname} got grade {grade} in {subject}")

    def calculate_average(self, subject=None):
        try:
            if subject:
                if subject not in self.grades or not self.grades[subject]:
                    return 0
                return statistics.mean(self.grades[subject])

            all_grades = []
            for g in self.grades.values():
                all_grades.extend(g)

            return statistics.mean(all_grades)
        except ValueError:
            return 0

    def __repr__(self):
        return super().__repr__() + f"Role: {self.__class__.__name__}\nClass: {self.class_name} Average grade: {self.calculate_average():.2f}\n"


class ElementaryStudent(Student):
    def __init__(self, firstname, lastname, personal_id_nr, date_of_birth, class_name, class_teacher):
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth, class_name)
        self.class_teacher = class_teacher
        self.hobbies = []

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)
        print(f"{self.fullname} participates in a: {hobby}")

    def __repr__(self):
        hobbies_text = ", ".join(self.hobbies) if self.hobbies else "None"
        return super().__repr__() + f"Class teacher: {self.class_teacher}\nHobbies: {hobbies_text}\n"


class HighSchoolStudent(Student):
    def __init__(self, firstname, lastname, personal_id_nr, date_of_birth, class_name, field_of_study):
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth, class_name)
        self.field_of_study = field_of_study
        self.chosen_subjects = []
        self.exams = {}

    def choose_subject(self, subject):
        self.chosen_subjects.append(subject)
        print(f"{self.fullname} participates in a: {subject}")

    def take_exam(self, subject, result):
        self.exams[subject] = result
        print(f"{self.fullname} took {subject} exam with results {result}")

    def __repr__(self):
        subjects_text = ", ".join(self.chosen_subjects) if self.chosen_subjects else "None"
        base = (
                super().__repr__() +
                f"Field of study: {self.field_of_study}\n"
                f"Chosen subjects: {subjects_text}\n"
        )
        if self.exams:
            base += f"Exam results: {self.exams}\n"
        return base


class Employee(Person, ABC):
    def __init__(self, firstname, lastname, personal_id_nr, date_of_birth, employee_id, position, salary):
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    @abstractmethod
    def calc_monthly_salary(self):
        pass

    def __repr__(self):
        return super().__repr__() + (f"Role: {self.__class__.__name__}\n"
                                     f"Employee ID: {self.employee_id}\n"
                                     f"Position: {self.position}\n"
                                     f"Monthly salary: {self.calc_monthly_salary():.2f}€\n")


class Teacher(Employee):
    def __init__(self, firstname, lastname, personal_id_nr, date_of_birth, employee_id, position, salary, subjects):
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth, employee_id, position, salary)
        self.subjects = subjects
        self.salary = salary
        self.lessons_per_week = 0
        self.students = []

    def teach_lesson(self, subject, class_name):
        if subject in self.subjects:
            self.lessons_per_week += 1
        print(f"{self.fullname} taught {subject} to class {class_name}")

    def calc_monthly_salary(self):
        return float(self.lessons_per_week * 25 + self.salary)

    def __repr__(self):
        subjects_text = ", ".join(self.subjects) if self.subjects else "None"
        return super().__repr__() + (f"Teacher subjects: {subjects_text}\n"
                                     f"Lessons per week: {self.lessons_per_week}\n")


class SubjectTeacher(Teacher):
    def __init__(self, firstname, lastname, personal_id_nr, date_of_birth, employee_id, salary, main_subject):
        position = f"{main_subject} teacher"
        subjects = [main_subject]
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth, employee_id, position, salary, subjects)
        self.salary = salary
        self.main_subject = main_subject
        self.set_specialization = ""

    def calc_monthly_salary(self):
        baas = super().calc_monthly_salary()
        if self.set_specialization:
            baas += 200
        return baas

    def __repr__(self):
        base = super().__repr__() + f"Main subject: {self.main_subject}\n"
        if self.set_specialization:
            base += f"Specialization: {self.set_specialization}\n"
        return base


class ClassTeacher(Teacher):
    def __init__(self, firstname, lastname, personal_id_nr, date_of_birth, employee_id, salary, subjects,
                 supervised_class):
        position = "Class teacher"
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth, employee_id, position, salary, subjects)
        self.supervised_class = supervised_class
        self.class_students = []

    def add_student_to_class(self, student):
        self.class_students.append(student)
        print(f"{student.fullname} added to {self.supervised_class} class\n")

    def calc_monthly_salary(self):
        palk = super().calc_monthly_salary() + 300 + (len(self.class_students) * 10)
        return palk

    def __repr__(self):
        return super().__repr__() + (f"Supervised class: {self.supervised_class}\n"
                                     f"Number of students: {len(self.class_students)}\n")


class SupportStaff(Employee):
    def __init__(self, firstname, lastname, personal_id_nr, date_of_birth, employee_id, position, salary,
                 responsibility_area):
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth, employee_id, position, salary)
        self.responsibility_area = responsibility_area
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"{self.fullname} sai uue ülesande: {task}")

    def calc_monthly_salary(self):
        # print(len(self.tasks))
        return (self.salary + len(self.tasks) * 20)

    def __repr__(self):
        if self.tasks:
            tasks_str = ", ".join(self.tasks)
            return super().__repr__() + f"Responsibility area: {self.responsibility_area}, Tasks: {tasks_str}"
        return super().__repr__() + f"Responsibility area: {self.responsibility_area}"


class School:
    def __init__(self, name, aadress):
        self.name = name
        self.address = aadress
        self.students = []
        self.employees = []
        self.classes = {}  # {klass_nimi: [Student]}
        self.subjects = []

    def add_student(self, student):
        self.students.append(student)
        if student.class_name not in self.classes:
            self.classes[student.class_name] = []
        self.classes[student.class_name].append(student)
        print(f"Student {student.fullname} added to {student.class_name} klassi")

    def add_employee(self, employee):
        self.employees.append(employee)
        if isinstance(employee, Teacher):
            for subj in employee.subjects:
                if subj not in self.subjects:
                    self.subjects.append(subj)
        print(f"Employee {employee.fullname} hired to {employee.position}")

    def display_all_people(self):
        print(f"\nSTUDENTS\n")
        for a in self.students:
            print(a.__repr__())
        print(f"\nEMPLOYEES\n")
        for b in self.employees:
            print(b.__repr__())

    def calculate_total_salary(self):
        palk = 0
        for a in self.employees:
            palk += a.calc_monthly_salary()
        return int(palk)
