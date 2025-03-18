DataFile = open("StudentsData.csv", "a")

# Prompt the user to enter values one by one or press Enter to quit
print("Enter student details (ID, Name, GPA) one by one or press Enter to quit")

# Start an infinite loop to get user input
while True:
    # Get input from the user for ID
    student_id = input("Enter ID: ")
    if student_id == "":
        break

    # Get input from the user for Name and enforce it to be entered
    student_name = input("Enter Name: ")
    while student_name == "":
        print("Name cannot be empty. Please enter a valid name.")
        student_name = input("Enter Name: ")

    # Get input from the user for GPA (can be left empty)
    student_gpa = input("Enter GPA (optional): ")

    # Write the student details to the file as a comma-separated line
    DataFile.write(f"{student_id},{student_name},{student_gpa}\n")

# Close the file
DataFile.close()