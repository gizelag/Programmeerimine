from datetime import datetime, date
import statistics
from abc import ABC, abstractmethod


# Person on BAASKLASS (parent class),
# mis kirjeldab ühist infot iga inimese kohta.
# Student ja Employee pärivad sellest klassist.
class Person:
    def __init__(self, firstname, lastname, personal_id_nr, date_of_birth):
        # Eesnimi ja perekonnanimi on tavalised isikuandmed
        self.firstname = firstname
        self.lastname = lastname

        # Isikukood – hoitakse lihtsalt väärtusena
        self.personal_id_nr = personal_id_nr

        # Sünnikuupäev teisendatakse stringist date objektiks,
        # et sellega saaks vanust arvutada
        self.date_of_birth = datetime.strptime(
            date_of_birth, "%Y-%m-%d"
        ).date()

    # PROPERTY – võimaldab täisnime kasutada nagu atribuuti,
    # kuigi tegelikult arvutatakse see jooksvalt
    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    # PROPERTY, mis arvutab vanuse dünaamiliselt
    # Vanust ei salvestata, vaid see arvutatakse alati uuesti
    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) <
            (self.date_of_birth.month, self.date_of_birth.day)
        )

    # __repr__ määrab, kuidas objekt kuvatakse printimisel
    def __repr__(self):
        return (
            f"Name: {self.fullname}\n"
            f"Age: {self.age}\n"
        )


# Student on ALAMKLASS, mis pärib Person klassist
# Ta kasutab Personi omadusi ja lisab õppimisega seotud loogika
class Student(Person):
    def __init__(self, firstname, lastname, personal_id_nr, date_of_birth, class_name):
        # super() kutsub vanemklassi konstruktorit
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth)

        # Klass, kus õpilane õpib (nt 7A)
        self.class_name = class_name

        # Sõnastik, kus hoitakse hindeid ainete kaupa
        self.grades = {}

    # Meetod uue hinde lisamiseks
    def add_grade(self, subject, grade):
        # Kontrollime, et hinne oleks lubatud vahemikus
        if 1 <= grade <= 5:
            # Kui ainet veel pole, loome selle
            if subject not in self.grades:
                self.grades[subject] = []

            self.grades[subject].append(grade)
            print(f"{self.firstname} got grade {grade} in {subject}")

    # Meetod keskmise arvutamiseks
    # Kui subject on None, arvutatakse kõikide hinnete keskmine
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
            # Kui hindeid ei ole
            return 0

    # POLÜMORFISM:
    # Student kirjutab üle Person klassi __repr__ meetodi
    def __repr__(self):
        return (
            super().__repr__() +
            f"Role: {self.__class__.__name__}\n"
            f"Class: {self.class_name}\n"
            f"Average grade: {self.calculate_average():.2f}\n"
        )


# ElementaryStudent on Student alamklass,
# mis lisab algklassidele iseloomulikud omadused
class ElementaryStudent(Student):
    def __init__(self, firstname, lastname, personal_id_nr,
                 date_of_birth, class_name, class_teacher):
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth, class_name)

        self.class_teacher = class_teacher
        self.hobbies = []

    # Meetod hobide lisamiseks
    def add_hobby(self, hobby):
        self.hobbies.append(hobby)
        print(f"{self.fullname} participates in: {hobby}")

    def __repr__(self):
        hobbies_text = ", ".join(self.hobbies) if self.hobbies else "None"
        return (
            super().__repr__() +
            f"Class teacher: {self.class_teacher}\n"
            f"Hobbies: {hobbies_text}\n"
        )


# HighSchoolStudent lisab gümnaasiumile omase info
class HighSchoolStudent(Student):
    def __init__(self, firstname, lastname, personal_id_nr,
                 date_of_birth, class_name, field_of_study):
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth, class_name)

        self.field_of_study = field_of_study
        self.chosen_subjects = []
        self.exams = {}

    def choose_subject(self, subject):
        self.chosen_subjects.append(subject)

    def take_exam(self, subject, result):
        self.exams[subject] = result

    def __repr__(self):
        subjects_text = ", ".join(self.chosen_subjects) if self.chosen_subjects else "None"
        text = (
            super().__repr__() +
            f"Field of study: {self.field_of_study}\n"
            f"Chosen subjects: {subjects_text}\n"
        )
        if self.exams:
            text += f"Exam results: {self.exams}\n"
        return text


# Employee on ABSTRAKTNE klass
# Seda ei saa otse kasutada, vaid ainult pärimise kaudu
class Employee(Person, ABC):
    def __init__(self, firstname, lastname, personal_id_nr,
                 date_of_birth, employee_id, position, salary):
        super().__init__(firstname, lastname, personal_id_nr, date_of_birth)

        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    # Abstraktne meetod – iga alamklass PEAB selle realiseerima
    @abstractmethod
    def calc_monthly_salary(self):
        pass

    def __repr__(self):
        return (
            super().__repr__() +
            f"Role: {self.__class__.__name__}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Position: {self.position}\n"
            f"Monthly salary: {self.calc_monthly_salary():.2f}€\n"
        )


# Teacher on Employee konkreetne realiseering
class Teacher(Employee):
    def __init__(self, firstname, lastname, personal_id_nr,
                 date_of_birth, employee_id, position, salary, subjects):
        super().__init__(firstname, lastname, personal_id_nr,
                         date_of_birth, employee_id, position, salary)

        self.subjects = subjects
        self.lessons_per_week = 0

    # Õpetaja võib anda ainult neid aineid, mida ta õpetab
    def teach_lesson(self, subject):
        if subject in self.subjects:
            self.lessons_per_week += 1

    # Abstraktse meetodi realiseerimine
    def calc_monthly_salary(self):
        return self.salary + self.lessons_per_week * 25

    def __repr__(self):
        subjects_text = ", ".join(self.subjects)
        return (
            super().__repr__() +
            f"Subjects: {subjects_text}\n"
            f"Lessons per week: {self.lessons_per_week}\n"
        )


# School koondab õpilased ja töötajad ühte süsteemi
class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address

        self.students = []
        self.employees = []
        self.classes = {}

    def add_student(self, student):
        self.students.append(student)

        if student.class_name not in self.classes:
            self.classes[student.class_name] = []

        self.classes[student.class_name].append(student)

    def add_employee(self, employee):
        self.employees.append(employee)

    # Näide polümorfismist:
    # kutsutakse sama meetodit erinevatel objektidel
    def calculate_total_salary(self):
        return sum(emp.calc_monthly_salary() for emp in self.employees)
#koigi tootajate palga summa kokku