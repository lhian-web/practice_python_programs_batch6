# Input text
text = input("Input your text here: ")

# Input ending word
ending_word = input("Input ending word here: ")

# Check if ending matches
if text[-len(ending_word):] == ending_word:
    print("Ending word matches") # Print result
else:
    print("Ending word not matches")
