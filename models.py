class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks


class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\n===== Student List =====")

        for student in self.students:
            print(f"ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Course: {student.course}")
            print(f"Marks: {student.marks}")
            print("----------------------")

    def search_student(self, keyword):
        found = False

        for student in self.students:
            if (student.student_id.lower() == keyword.lower()
                    or student.name.lower() == keyword.lower()):

                print("\nStudent Found:")
                print(f"ID: {student.student_id}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Course: {student.course}")
                print(f"Marks: {student.marks}")

                found = True

        if not found:
            print("Student not found.")

    def update_student(self, student_id):
        for student in self.students:

            if student.student_id == student_id:

                print("Enter new details:")

                student.name = input("Enter new name: ")
                student.age = int(input("Enter new age: "))
                student.course = input("Enter new course: ")
                student.marks = float(input("Enter new marks: "))

                print("Student updated successfully!")
                return

        print("Student not found.")

    def delete_student(self, student_id):
        for student in self.students:

            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found.")