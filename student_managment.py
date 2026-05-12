
class StudentManagement:

    
    students = [
        {"id": 101, "name": "Aarav Patel", "class": "BCA 1"},
        {"id": 102, "name": "Diya Shah", "class": "BCA 1"},
        {"id": 103, "name": "Vivaan Mehta", "class": "BCA 2"}
    ]

    def __init__(self):
        pass

    def add_student(self):

        student_id = int(input("Enter Student ID: "))
        student_name = input("Enter Student Name: ")
        student_class = input("Enter Student Class: ")

        new_student = {
            "id": student_id,
            "name": student_name,
            "class": student_class
        }

        StudentManagement.students.append(new_student)

        print(f"\nStudent {student_name} added successfully.\n")

    def remove_student(self):

        student_name = input("Enter student name to remove: ")

        for student in StudentManagement.students:

            if student["name"].lower() == student_name.lower():
                StudentManagement.students.remove(student)
                print(f"\nStudent {student_name} removed successfully.\n")
                return

        print("\nStudent not found.\n")

    def display_students(self):

        print("\nStudent List:")

        for student in StudentManagement.students:
            print(student)

    def save_students(self):

     with open("student_report.txt", "w") as file:
        file.write("Student Management Report\n")
        file.write("=========================\n\n")

        for student in StudentManagement.students:
            file.write(f"ID: {student['id']}, Name: {student['name']}, Class: {student['class']}\n")

        print("\nStudents saved successfully to file!\n")
    def menu(self):

        while True:
            print("\n1. Add Student")
            print("2. Remove Student")
            print("3. Display Students")
            print("4. Save Students report")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.display_students()
            elif choice == "4":
                self.save_students()
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice")



obj = StudentManagement()
obj.menu()






