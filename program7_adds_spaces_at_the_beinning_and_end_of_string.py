# Input text
text = input("Enter text: ")

# Length limit
limit = int(input("Enter length limit: "))

spaces = limit - len(text)

left = spaces // 2
right = spaces -left

# Add spaces on both sides
for i in range(left):
    text = " " + text

for i in range(right):
    text = text + " "

# Print
print(text)