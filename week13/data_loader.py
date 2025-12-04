import csv
from school_system import ElementaryStudent
from school_system import HighSchoolStudent
from school_system import SubjectTeacher
from school_system import ClassTeacher
from school_system import SupportStaff
class DataLoader():

    @staticmethod
    def load_elementary_students(filename='elementary_students.csv'):
        ElementaryStudent_list = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = csv.DictReader(f)

                for row in data:
                    student = ElementaryStudent(
                        firstname=row['firstname'].strip(),
                        lastname=row['lastname'].strip(),
                        personal_id_nr=int(row['personal_id_nr'].strip()),
                        date_of_birth=row['date_of_birth'].strip(),
                        class_name=row['class_name'].strip(),
                        class_teacher=row['class_teacher'].strip()
                    )
                    ElementaryStudent_list.append(student)

        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
        õpilaste_arv = len(ElementaryStudent_list)

        print(f"Elementary school õpilaste kogu arv: {õpilaste_arv}")
        return ElementaryStudent_list


    @staticmethod
    def load_high_school_students(filename='high_school_students.csv'):
        high_school_list = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = csv.DictReader(f)

                for row in data:
                    student = HighSchoolStudent(
                        firstname=row['firstname'].strip(),
                        lastname=row['lastname'].strip(),
                        personal_id_nr=int(row['personal_id_nr'].strip()),
                        date_of_birth=row['date_of_birth'].strip(),
                        class_name=row['class_name'].strip(),
                        field_of_study=row['field_of_study'].strip()
                    )
                    high_school_list.append(student)

        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
        õpilaste_arv = len(high_school_list)
        print(f"Highschool Õpilaste kogu arv: {õpilaste_arv}")
        return high_school_list

    @staticmethod
    def load_subject_teachers(filename='subject_teachers.csv'):
        subject_teachers = []

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = csv.DictReader(f)

                for row in data:
                    firstname = row.get('firstname') or row.get('first_name')
                    lastname = row.get('lastname') or row.get('last_name')
                    personal_id_nr = row.get('personal_id_nr') or "00000000000"
                    date_of_birth = row.get('date_of_birth') or "1900-01-01"
                    employee_id = row.get('employee_id') or "UNKNOWN"
                    salary = row.get('salary') or "0"
                    main_subject = row.get('main_subject') or row.get('subject')

                    teacher = SubjectTeacher(
                        firstname=firstname.strip(),
                        lastname=lastname.strip(),
                        personal_id_nr=int(str(personal_id_nr).strip()),
                        date_of_birth=str(date_of_birth).strip(),
                        employee_id=str(employee_id).strip(),
                        salary=float(salary),
                        main_subject=str(main_subject).strip()
                    )
                    subject_teachers.append(teacher)

        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"Error loading subject teachers: {e}")

        return subject_teachers

    @staticmethod
    def load_class_teachers(filename='class_teachers.csv'):
        class_teachers = []

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = csv.DictReader(f)
                for row in data:
                    student = ClassTeacher(
                        firstname=row['firstname'].strip(),
                        lastname=row['lastname'].strip(),
                        personal_id_nr=int(row['personal_id_nr'].strip()),
                        date_of_birth=row['date_of_birth'].strip(),
                        employee_id=row['employee_id'].strip(),
                        salary=int(row['salary'].strip()),
                        subjects=row["subjects"].strip().split(";"),
                        supervised_class=row['supervised_class'].strip()
                    )
                    class_teachers.append(student)

        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
        class_teachers_arv = len(class_teachers)
        print(f"Class teachers kogu arv: {class_teachers_arv}")
        return class_teachers

    @staticmethod
    def load_support_staff(filename='support_staff.csv'):
        support_staff = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = csv.DictReader(f)

                for row in data:
                    student = SupportStaff(
                        firstname=row['firstname'].strip(),
                        lastname=row['lastname'].strip(),
                        personal_id_nr=int(row['personal_id_nr'].strip()),
                        date_of_birth=row['date_of_birth'].strip(),
                        employee_id=row['employee_id'].strip(),
                        position=row['position'].strip(),
                        salary=int(row['salary'].strip()),
                        responsibility_area=row['responsibility_area'].strip()
                    )

                    support_staff.append(student)

        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
        support_staff_arv = len(support_staff)
        print(f"Support staff kogu arv: {support_staff_arv}")
        return support_staff

    @staticmethod
    def load_all_data(elementary_data="elementary_students.csv",
                      high_school_data="high_school_students.csv",
                      subject_teachers_data="subject_teachers.csv",
                      class_teachers_data="class_teachers.csv",
                      support_staff_data="support_staff.csv"):
        return {
            'elementary_students': DataLoader.load_elementary_students(elementary_data),
            'high_school_students': DataLoader.load_high_school_students(high_school_data),
            'subject_teachers': DataLoader.load_subject_teachers(subject_teachers_data),
            'class_teachers': DataLoader.load_class_teachers(class_teachers_data),
            'support_staff': DataLoader.load_support_staff(support_staff_data)
        }

if __name__ == '__main__':
    data = DataLoader.load_all_data()
    print(data)
