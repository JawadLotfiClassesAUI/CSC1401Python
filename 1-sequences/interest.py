# Prompt the user to enter the principal amount and convert the input to a float
principal = float(input("Enter the principal:"))
# Prompt the user to enter the interest rate and convert the input to a float
rate = float(input("Enter the interest rate:"))
# Prompt the user to enter the duration in years and convert the input to an integer
years = int(input("Enter the duration in years:"))

# Calculate the accumulated interest
interest = principal * (rate/100) * years

# Display the accumulated interest
print(f"The accumulated interest is {interest} dirhams")

# Wait for the user to press enter before quitting
input("Press Enter to quit")