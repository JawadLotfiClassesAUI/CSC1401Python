message = input("Enter any message you want:")

# Print the length of the message
print(f"The length is {len(message)}")

# Convert the message to uppercase
print(message.upper())
# Capitalize the first letter of the message
print(message.capitalize())
# Convert the first letter of each word to uppercase
print(message.title())
# Convert the message to lowercase
print(message.lower())

# Replace all occurrences of 'e' with '#'
print(message.replace("e", "#"))
# Count the number of times 'e' appears in the message
print(message.count("e"))
# Find the first occurrence of 'e' in the message
print(message.find("e"))
# Check if the message ends with 'e'
print(message.endswith("e"))