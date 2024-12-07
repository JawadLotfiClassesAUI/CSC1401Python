# Inputs
# Prompt the user to enter the number of products and convert the input to an integer
products = int(input("Enter the number of products"))
# Prompt the user to enter the number of customers and convert the input to an integer
customers = int(input("Enter the number of customers"))

# Processes
# Calculate the number of products each customer gets using integer division
prodPerCustomer = products // customers
# Calculate the number of products left after distribution using the modulus operator
productsLeft = products % customers

# Outputs
# Display the number of products each customer gets
print(f"There are {prodPerCustomer} products per customer")
# Display the number of products left
print(f"There are {productsLeft} products left")

# Wait for the user to press enter before quitting
input("Press enter to quit")