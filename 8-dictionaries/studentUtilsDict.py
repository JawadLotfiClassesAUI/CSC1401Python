def printMenu():
    print("1. Add student")
    print("2. View students")
    print("3. Delete student")
    print("4. Quit")
    print("5. Display statistics")

def add_student(listOfStudents):
    student = {}
    student['id'] = input("Enter student ID: ")
    student['name'] = input("Enter student name: ")
    student['gpa'] = float(input("Enter student GPA: "))
    listOfStudents.append(student)

def view_students(listOfStudents):
    print(f"{'ID':<10} {'Name':<20} {'GPA':<5}")
    for student in listOfStudents:
        print(f"{student['id']:<10} {student['name']:<20} {student['gpa']:<5}")

def delete_student(listOfStudents):
    id = input("Enter student ID to delete: ")
    for student in listOfStudents:
        if student['id'] == id:
            listOfStudents.remove(student)
            print("Student data deleted.")
            return
    print("Student ID not found.")

def display_statistics(listOfStudents):
    if len(listOfStudents) == 0:
        print("No student data available.")
    else:
        listOfGPAs = []
        for student in listOfStudents:
            listOfGPAs.append(student['gpa'])
        print(f"Highest GPA: {max(listOfGPAs)}")
        print(f"Lowest GPA: {min(listOfGPAs)}")
        print(f"Average GPA: {sum(listOfGPAs) / len(listOfGPAs):.2f}")
        print(f"Number of students: {len(listOfStudents)}")
