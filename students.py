from fileManager import FileManager


class Students:
    students = []
    file_manager = FileManager()

    def get_students_titlecase(self):
        students_titlecase = []
        for student in self.students:
            students_titlecase.append(student["name"].title())
        return students_titlecase

    def print_students_titlecase(self):
        return self.get_students_titlecase()

    def add_student(self, name, student_id=123):
        student = {"name": name, "student_id": student_id}
        self.students.append(student)

    def read_file(self):
        try:
            result = self.file_manager.read_file("students.txt")
            if result:
                for student in result:
                    self.add_student(student)
        except Exception:
            print("Exception raised when reading file with Student Data")

    def save_file(self):
        try:
            for student in self.students:
                self.file_manager.save_file(student["name"], "students.txt")
        except Exception:
            print("Exception raised when saving file with Student Data")


manuel = Students()
# manuel.add_student("Manuel")
# manuel.save_file()

manuel.read_file()
print(manuel.print_students_titlecase())
