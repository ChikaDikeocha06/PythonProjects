#Example of Looping to count 
words = ["cat", "dog", "elephant"]
total_chars = 0  # start counter

for word in words:  # loop through words
    total_chars += len(word)  # add length of each word

print("Total characters:", total_chars)