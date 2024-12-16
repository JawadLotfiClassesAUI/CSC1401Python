# Method 1: Using 5 parallel lists (partially scalable)
quiz1 = []
quiz2 = []
quiz3 = []
quiz4 = []
quiz5 = []

numOfStudents = 30

for s in range(numOfStudents):
    quiz1.append(float(input(f"Enter grade for student {s+1} in quiz 1: ")))
    quiz2.append(float(input(f"Enter grade for student {s+1} in quiz 2: ")))
    quiz3.append(float(input(f"Enter grade for student {s+1} in quiz 3: ")))
    quiz4.append(float(input(f"Enter grade for student {s+1} in quiz 4: ")))
    quiz5.append(float(input(f"Enter grade for student {s+1} in quiz 5: ")))

print("All grades using parallel lists:")
for s in range(numOfStudents):
    print(f"Student {s+1}: {quiz1[s]}, {quiz2[s]}, {quiz3[s]}, {quiz4[s]}, {quiz5[s]}")

# Method 2: Using a 2-dimensional list (fully scalable)
grades = []  # Correctly initialize an empty list
numOfQuizzes = 5
for s in range(numOfStudents):
    grades.append([])  # Append an empty sublist for each student
    for q in range(numOfQuizzes):
        grades[s].append(float(input(f"Enter grade for student {s+1} in quiz {q+1}: ")))

print("All grades using a 2-dimensional list:")
for s in range(30):
    print(f"Student {s+1}: {grades[s]}")