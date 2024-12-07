# Functional decomposition helps in managing this nested selection situation by breaking down the complex problem into smaller, more manageable functions. 
# This improves code readability, maintainability, and reusability, making it easier to debug and extend.

# Main function definition
def main():
    # Function call
    category = input("Choose a category (electronics/clothing): ").lower()
    if category == "electronics":
        # Function call
        electronics_selection()
    elif category == "clothing":
        # Function call
        clothing_selection()
    else:
        print("Invalid category.")

# Function definition
def electronics_selection():
    subcategory = input("Choose a subcategory (phones/laptops): ").lower()
    if subcategory == "phones":
        product = input("Choose a product (iPhone/Samsung): ").lower()
        if product == "iphone":
            print("You selected iPhone.")
        elif product == "samsung":
            print("You selected Samsung.")
        else:
            print("Invalid product.")
    elif subcategory == "laptops":
        product = input("Choose a product (MacBook/Dell): ").lower()
        if product == "macbook":
            print("You selected MacBook.")
        elif product == "dell":
            print("You selected Dell.")
        else:
            print("Invalid product.")
    else:
        print("Invalid subcategory.")

# Function definition
def clothing_selection():
    subcategory = input("Choose a subcategory (men/women): ").lower()
    if subcategory == "men":
        product = input("Choose a product (shirt/pants): ").lower()
        if product == "shirt":
            print("You selected a men's shirt.")
        elif product == "pants":
            print("You selected men's pants.")
        else:
            print("Invalid product.")
    elif subcategory == "women":
        product = input("Choose a product (dress/skirt): ").lower()
        if product == "dress":
            print("You selected a dress.")
        elif product == "skirt":
            print("You selected a skirt.")
        else:
            print("Invalid product.")
    else:
        print("Invalid subcategory.")

# Function call
main()