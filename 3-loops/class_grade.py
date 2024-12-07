# Initialize total sum of grades and counter for number of grades
total = 0
counter = 0

# Prompt user to enter the first grade or '=' to stop
grade = input("Enter a grade of student or = to stop:")

# Loop until the user enters '='
while grade != "=":
    # Increase the total sum by the entered grade
    total += float(grade)
    # Increment the counter by 1 to account for the entered grade
    counter += 1
    # Allow the user to control the loop by entering the next grade or '=' to stop
    grade = input("Enter a grade of student or = to stop:")

# Check if any grades were entered
if counter > 0:
    # Calculate the average of the grades
    average = total / counter
    # Print the average of the grades
    print(f"The average of the grades is {average}")
else:
    # Print a message if no grades were entered
    print("You didn't enter any grade")