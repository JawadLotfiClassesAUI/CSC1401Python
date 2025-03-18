message = input("Enter any message you want:")
vowelsCount = 0
# count and display the vowels in the string
for char in message:  # Loop through each character in the input message
    if char == 'a' or char == 'A':  # Check if the character is 'a' or 'A'
        vowelsCount += 1
    elif char == 'e' or char == 'E':  # Check if the character is 'e' or 'E'
        vowelsCount += 1
    elif char == 'i' or char == 'I':  # Check if the character is 'i' or 'I'
        vowelsCount += 1
    elif char == 'o' or char == 'O':  # Check if the character is 'o' or 'O'
        vowelsCount += 1
    elif char == 'u' or char == 'U':  # Check if the character is 'u' or 'U'
        vowelsCount += 1
print(f"There are {vowelsCount} vowels in this message")