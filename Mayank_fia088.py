def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
print("You are running the first requirement of word count now")
val = input("Enter your Words: ")
print(word_count(val))
print("\n")




# Second requirement

import re
print("Now the second requirement is executing")
val = input("Enter your string : ")
x = input("Enter the word to replace : ")
y = input("Enter the word to replace with : ")

print("Your final sentence is : " +re.sub(x, y, val))