# Input text
text = input("Please input your text here: ")
# Which word to remove
word_remove = input("Please input the word to remove here: ")

# Check if it matches first word in the text
if text[0:len(word_remove)] == word_remove:
    result = text[len(word_remove):]

    if result[0] == " ":
        result = result[1:]

else:
    result = text

# Print
print(result)