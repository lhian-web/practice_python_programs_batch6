# Input text
text = input("Enter a text: ")

# Specify length
limit = int(input("Enter length limit: "))

# Add spaces until specified length is reached
while len(text) < limit:
    text = text + " "

# Print result
print(text)