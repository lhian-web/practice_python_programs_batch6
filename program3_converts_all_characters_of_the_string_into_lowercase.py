# Input text
text = input("Enter your text here: ")

result = ""

# Convert uppercase to lowercase
for char in text:
    if char >= "A" and char <= "Z":
        result = result + chr(ord(char) + 32)
    else:
        result = result + char

# print result
print(result)