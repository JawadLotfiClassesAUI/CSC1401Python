# Get user input for main category
category = input("Choose a category (electronics/clothing): ").lower()

# Outer selection
if category == "electronics":
    # Nested selection for subcategory
    subcategory = input("Choose a subcategory (phones/laptops): ").lower()
    if subcategory == "phones":
        # Nested selection for product
        product = input("Choose a product (iPhone/Samsung): ").lower()
        if product == "iphone":
            print("You selected iPhone.")
        elif product == "samsung":
            print("You selected Samsung.")
        else:
            print("Invalid product.")
    elif subcategory == "laptops":
        # Nested selection for product
        product = input("Choose a product (MacBook/Dell): ").lower()
        if product == "macbook":
            print("You selected MacBook.")
        elif product == "dell":
            print("You selected Dell.")
        else:
            print("Invalid product.")
    else:
        print("Invalid subcategory.")
elif category == "clothing":
    # Nested selection for subcategory
    subcategory = input("Choose a subcategory (men/women): ").lower()
    if subcategory == "men":
        # Nested selection for product
        product = input("Choose a product (shirt/pants): ").lower()
        if product == "shirt":
            print("You selected a men's shirt.")
        elif product == "pants":
            print("You selected men's pants.")
        else:
            print("Invalid product.")
    elif subcategory == "women":
        # Nested selection for product
        product = input("Choose a product (dress/skirt): ").lower()
        if product == "dress":
            print("You selected a dress.")
        elif product == "skirt":
            print("You selected a skirt.")
        else:
            print("Invalid product.")
    else:
        print("Invalid subcategory.")
else:
    print("Invalid category.")
