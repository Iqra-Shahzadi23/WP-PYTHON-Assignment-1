# -----------------------------
# Student Management System
# -----------------------------

students = []


# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


# Function to add a student
def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ")

    # Check if ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")

    while True:
        try:
            age = int(input("Enter Age: "))
            if age > 0:
                break
            else:
                print("Age must be greater than 0.")
        except ValueError:
            print("Please enter a valid age.")

    course = input("Enter Course: ")

    while True:
        try:
            marks = float(input("Enter Marks (0-100): "))
            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter valid marks.")

    grade = calculate_grade(marks)

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "grade": grade
    }

    students.append(student)

    print("Student added successfully!\n")


# Function to display all students
def view_students():
    print("\n--- Student Records ---")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("-" * 40)
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Course     :", student["course"])
        print("Marks      :", student["marks"])
        print("Grade      :", student["grade"])
    print("-" * 40)


# Function to search a student
def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print("-" * 40)
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Course     :", student["course"])
            print("Marks      :", student["marks"])
            print("Grade      :", student["grade"])
            print("-" * 40)
            return

    print("Student not found.")


# Function to update student
def update_student():
    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            student["name"] = input("Enter New Name: ")

            while True:
                try:
                    age = int(input("Enter New Age: "))
                    if age > 0:
                        student["age"] = age
                        break
                    else:
                        print("Age must be greater than 0.")
                except ValueError:
                    print("Invalid age.")

            student["course"] = input("Enter New Course: ")

            while True:
                try:
                    marks = float(input("Enter New Marks: "))
                    if 0 <= marks <= 100:
                        student["marks"] = marks
                        student["grade"] = calculate_grade(marks)
                        break
                    else:
                        print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Invalid marks.")

            print("Student information updated successfully.")
            return

    print("Student not found.")


# Function to delete student
def delete_student():
    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


# Main menu
def main():

    while True:

        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

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
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")


# Program starts here
main()