# Function to handle the checkout process for a single checkout
def handleCheckout(checkout):
    print(f"Handling checkout #{checkout}")
    subTotal = 0
    price = float(input("Enter the price of your product:"))

    # Loop to process each product's price until 0 is entered
    while price != 0:
        subTotal += price
        price = float(input("Enter the price of your product:"))

    print(f"The sub total for checkout #{checkout} is {subTotal}")
    return subTotal

# Main function to handle multiple checkouts
def main():
    numCheckouts = int(input("How many checkouts do you have? "))
    grandTotal = 0

    # Loop to process each checkout
    for checkout in range(1, numCheckouts+1):
        # Call the handleCheckout function and add the returned subtotal to the grand total
        grandTotal += handleCheckout(checkout)

    print(f"The grand total is {grandTotal}")

# Call the main function to start the program
main()