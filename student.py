students = {}


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    for student_id, details in students.items():
        print("\nStudent ID:", student_id)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Course:", details["course"])


def search_student():
    student_id = input("Enter Student ID to search: ")

    if student_id in students:
        details = students[student_id]

        print("\nStudent Found")
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Course:", details["course"])
    else:
        print("Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ")

    if student_id in students:
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ")

        students[student_id] = {
            "name": name,
            "age": age,
            "course": course
        }

        print("Student updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
