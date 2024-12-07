numCheckouts = int(input("How many checkouts do you have? "))
# Initializing the grand total to 0
grandTotal = 0

#Outer loop handling the checkouts - Definite
for checkout in range(1, numCheckouts+1):
    print(f"Handling checkout #{checkout}")
    # Initializing/Resetting the sub total to 0
    subTotal = 0
    price = float(input("Enter the price of your product:"))

    # Inner loop handling the prices - Indefinite
    while price != 0:
        # Updating the sub total
        subTotal += price
        price = float(input("Enter the price of your product:"))

    print(f"The sub total for checkout #{checkout} is {subTotal}")
    # updating the grand total
    grandTotal += subTotal

print(f"The grand total is {grandTotal}")