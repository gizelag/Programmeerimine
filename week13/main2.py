from data_loader import DataLoader
from school_system import School


def main():
    school = School("Tallinn Real Gymnasium", "Estonia pst 1, Tallinn")
    objektid = DataLoader.load_all_data()
    #print(f"1{objektid}2")
    #Hobid
    elementary = objektid.get("elementary_students", [])
    highschool = objektid.get("high_school_students", [])
    subject_teachers = objektid.get("subject_teachers", [])
    class_teachers = objektid.get("class_teachers", [])
    support_staff = objektid.get("support_staff", [])

    # Leia vajalikud isikud turvaliselt
    mari = next((s for s in elementary if s.firstname.lower() == "mari"), None)
    juku = next((s for s in elementary if s.firstname.lower() == "juku"), None)

    anna = next((s for s in highschool if s.firstname.lower() == "anna"), None)
    peeter = next((s for s in highschool if s.firstname.lower() == "peeter"), None)
    markus = next((s for s in highschool if s.firstname.lower() == "markus"), None)

    toomas = next((t for t in subject_teachers if t.firstname.lower() == "toomas"), None)
    liisa = next((t for t in subject_teachers if t.firstname.lower() == "liisa"), None)

    kati = next((t for t in class_teachers if t.firstname.lower() == "kati"), None)

    jaan = next((ss for ss in support_staff if ss.firstname.lower() == "jaan"), None)

    print("\n*** Setting additional data ***\n")

    # Elementary – hobid ja hinded
    if mari:
        mari.add_hobby("Volleyball")
        mari.add_grade("Mathematics", 4)
        mari.add_grade("Estonian", 5)

    if juku:
        juku.add_hobby("Football")
        juku.add_hobby("Robotics")
        juku.add_grade("Mathematics", 5)
        juku.add_grade("Physics", 5)
        juku.add_grade("Estonian", 3)

    # Highschool – ained, hinded, eksamid
    if anna:
        anna.choose_subject("Physics")
        anna.choose_subject("Mathematics")
        anna.add_grade("Chemistry", 4)
        anna.add_grade("Biology", 3)
        anna.take_exam("Mathematics", 96)

    if peeter:
        peeter.choose_subject("English")
        peeter.add_grade("Society", 5)
        peeter.add_grade("Estonian", 3)
        peeter.add_grade("Chemistry", 2)
        peeter.take_exam("Estonian", 85)

    if markus:
        markus.choose_subject("English")
        markus.choose_subject("Physics")
        markus.add_grade("Biology", 5)
        markus.add_grade("Estonian", 3)
        markus.add_grade("History", 4)
        markus.add_grade("Chemistry", 5)
        markus.take_exam("Mathematics", 74)
        markus.take_exam("Estonian", 78)

    # SubjectTeacher specialization
    if toomas:
        toomas.set_specialization = "Geometry"
        print(f"{toomas.fullname} specialized in: Geometry")

    # SupportStaff tasks
    if jaan:
        jaan.add_task("Cleaning classrooms")
        jaan.add_task("Washing windows")

    print("\n*** Staffing the school ***\n")

    # Kõik õpilased kooli
    for s in elementary:
        school.add_student(s)
    for s in highschool:
        school.add_student(s)

    # Kõik töötajad kooli
    for t in class_teachers:
        school.add_employee(t)
    for t in subject_teachers:
        school.add_employee(t)
    for ss in support_staff:
        school.add_employee(ss)

    # Õpilaste lisamine klassi
    if kati and mari:
        kati.add_student_to_class(mari)
    if kati and juku:
        kati.add_student_to_class(juku)

    # Õpetamised
    if toomas:
        toomas.teach_lesson("Math", "3a")
        toomas.teach_lesson("Math", "11a")

    if liisa:
        liisa.teach_lesson("Physics", "11a")

    print("\n*** All Persons info ***\n")
    print(f"=== {school.name} - All people ===\n")
    school.display_all_people()

    print(f"\n*** Total salary: ***\nTotal monthly salary: {school.calculate_total_salary():.2f}€")


if __name__ == "__main__":
    main()