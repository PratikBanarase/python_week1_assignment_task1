from models import Student, StudentManager
manager = StudentManager()
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":

        student_id = input("Enter student ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))

        student = Student(
          student_id,
          name,
          age,
          course,
          marks
        )

        manager.add_student(student)
    elif choice == "2":
        manager.view_students()    
    elif choice == "3":
        keyword = input("Enter student ID or name: ")
        manager.search_student(keyword)    
    elif choice == "4":
        student_id = input("Enter student ID to update: ")
        manager.update_student(student_id)    
    elif choice == "5":
        student_id = input("Enter student ID to delete: ")
        manager.delete_student(student_id)    
    elif choice == "6":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice. Please select 1-6.")    