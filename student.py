
students = []

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    course = input("Enter course: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Course": course
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(
            f"ID: {student['ID']}, "
            f"Name: {student['Name']}, "
            f"Course: {student['Course']}"
        )

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting application.")
        break
    else:
        print("Invalid choice. Try again.")
