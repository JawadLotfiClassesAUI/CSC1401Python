# This program displays the squares
# of numbers in a user-defined range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
increment = int(input("Enter the increment: "))

# Note: The end value is usually excluded in the range function, so we add 1 to include it
for counter in range(start, end + 1, increment):
    print(f"The square of {counter} is {counter ** 2}")