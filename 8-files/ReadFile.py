import os

# Check if the file exists before opening it
if os.path.exists("StudentsData.csv"):
    studentsFile = open("StudentsData.csv", "r")

    for line in studentsFile:
        # Find the positions of the first and second commas
        firstComma = line.find(',')
        # The second parameter in find specifies the starting position for the search, which is just after the first comma
        secondComma = line.find(',', firstComma + 1)
        
        # Extract substrings based on the positions of the commas using slicing
        id = line[:firstComma]
        name = line[firstComma + 1:secondComma]
        # Use .strip() to remove any leading or trailing whitespace characters (spaces, tabs, newlines)
        gpa = line[secondComma + 1:].strip()
        
        print(f"ID: {id}, Name: {name}, GPA: {gpa}")

    studentsFile.close()
else:
    # Print an error message if the file is not found
    print("File not found")