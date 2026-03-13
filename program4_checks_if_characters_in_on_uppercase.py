# Input text
text = input("Enter your text here: ")

upper = True

# Check characters
for char in text:
    if char >= 'a' and char <= 'z':
        upper = False

# Print result
print(upper)