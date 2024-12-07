year = int(input("Enter the year number:"))

# Combining conditions into a longer expression helps to make the code more concise and readable.
# Instead of using multiple if-else statements, we can use logical operators (and, or) to combine conditions.
# This reduces the number of lines of code and makes the logic easier to follow.
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("The year is leap")
else:
    print("The year is not leap")