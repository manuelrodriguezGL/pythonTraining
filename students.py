students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase


def print_students_titlecase():
    return get_students_titlecase()


def add_student(name, student_id=123):
    student = {"name": name, "student_id": student_id}
    students.append(student)

