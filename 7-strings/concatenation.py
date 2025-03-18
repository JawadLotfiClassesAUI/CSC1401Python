inputString = input("Enter your string:")
finalString = ""

# Calculate the stopping index for the loop (negative length of the input string)
stop = -len(inputString)

# Loop through the input string in reverse using negative indexing
for index in range(-1, stop-1, -1):
    # Concatenate each character to the finalString to build the reversed string
    finalString = finalString + inputString[index]

# Print the reversed string
print(finalString)

# Check if the input string is a palindrome
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
# For example, "madam" and "racecar" are palindromes.
if inputString == finalString:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")