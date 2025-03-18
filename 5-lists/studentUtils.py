def printMenu():
    # Display the menu options to the user
    print("\nMenu:")
    print("1. Add student data")
    print("2. View all students data")
    print("3. Delete a student's data by ID")
    print("4. Quit")

def add_student(ids, names, gpas):
    # Prompt the user to enter student details and add them to the lists
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    gpa = float(input("Enter student GPA: "))
    # Append the new student data to the respective lists
    ids.append(id)
    names.append(name)
    gpas.append(gpa)

def view_students(ids, names, gpas):
    # Display all students' data in a tabular format with aligned columns using f-strings
    print(f"{'ID':<10} {'Name':<20} {'GPA':<5}")
    for i in range(len(ids)):
        print(f"{ids[i]:<10} {names[i]:<20} {gpas[i]:<5}")

def delete_student(ids, names, gpas):
    # Prompt the user to enter a student ID and delete the corresponding data
    id = input("Enter student ID to delete: ")
    # Check if the entered ID exists in the ids list
    if id in ids:
        # Find the index of the student ID in the list
        index = ids.index(id)
        # Remove the student data from the lists using the index
        ids.pop(index)
        names.pop(index)
        gpas.pop(index)
        print("Student data deleted.")
    else:
        print("Student ID not found.")

def display_statistics(gpas):
    if len(gpas) == 0:
        print("No student data available.")
    else:
        print(f"Highest GPA: {max(gpas)}")
        print(f"Lowest GPA: {min(gpas)}")
        print(f"Average GPA: {sum(gpas) / len(gpas):.2f}") # Display average GPA with 2 decimal places
        print(f"Number of students: {len(gpas)}")