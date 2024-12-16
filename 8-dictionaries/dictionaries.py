# Simple example of a dictionary to handle student data
student = {
    "name": "John Doe",
    "id": "12345",
    "gpa": 3.8
}

# Print the student dictionary
print("Single student data:", student)

# More elaborate list of students
listOfStudents = [
    {"name": "John Doe", "id": "12345", "gpa": 3.8},
    {"name": "Jane Smith", "id": "67890", "gpa": 3.9},
    {"name": "Emily Davis", "id": "54321", "gpa": 3.7}
]

# Print the list of students
print("List of students:")
for student in listOfStudents:
    print(student)
