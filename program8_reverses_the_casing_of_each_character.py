# Input text
text = input("Enter text: ")
result = ""

# Check each character
for char in text:
    if char >= 'A' and char <= 'Z':
        result = result + chr(ord(char) + 32)

    elif char >= 'a' and char <= 'z':
        result = result + chr(ord(char) - 32)

    else:
        result = result + char

# Print result
print(result)