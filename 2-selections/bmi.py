weight = float(input("Enter your weight (kgs):"))
height = float(input("Enter your height (cms):"))

# Calculate BMI
bmi = weight / (height/100) ** 2

# Check BMI category
if 0 < bmi < 18.5:
    # BMI is low
    print("The body mass index is low")
elif 18.5 <= bmi and bmi < 25:
    # BMI is average
    print("The body mass index is average")
elif bmi >= 25:
    # BMI is high
    print("The body mass index is high")
else:
    # BMI is incorrect
    print("Incorrect Body mass index")