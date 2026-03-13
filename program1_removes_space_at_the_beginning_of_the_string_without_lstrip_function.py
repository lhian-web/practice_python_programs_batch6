# input text
text = input("Please input your text with spaces at th beginning: ")

# check each character
start = False

for char in text:
    if char != " ":
        start = True

    if start: # print
        print(char, end="")