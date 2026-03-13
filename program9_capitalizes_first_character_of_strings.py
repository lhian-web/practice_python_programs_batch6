# Input text
text = input("Enter text: ")
result = ""

# Check each character
for i in range(len(text)):
    char = text[i]

    # Convert letters
    if i == 0 and char >= "a" and char <= "z":
        result = result + chr(ord(char) - 32)

    elif i > 0 and char >= "A" and char <= "Z":
        result = result + chr(ord(char) + 32)

    else:
        result = result + char

# print result
print(result)