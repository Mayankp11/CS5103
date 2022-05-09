# First requirement

# word_count is used to count words in the string
def word_count(str):
    # create an empty dictionary
    counts = dict()
    # To split the lines into words
    words = str.split()
    # To iterate over each word in string
    for word in words:
        # To check if word is already present in the dictionary
        if word in counts:
            # To increment count of word by 1
            counts[word] += 1
        else:
            # Add the word to dictionary
            counts[word] = 1
    #returning the count now
    return counts

#here running the first requirement
print("You are running the first requirement of word count now")
val = input("Enter your Words: ")
print(word_count(val))
print("\n")




# Second requirement

# To import  python regular expression library
import re
print("Now the second requirement is executing")
val = input("Enter your string : ")
source = input("Enter the word to replace : ")
final = input("Enter the word to replace with : ")


if source in val:
        print("Your final sentence is : " +re.sub(source, final, val))
else: print("Cannot change")


#3rd req
import re



print('\n')
print("The third requirement")
txt = "The rain in Spain"



x = re.findall(r'\bRain\b', txt,flags=re.IGNORECASE)
print(x)

if (x):
    print("Yes, there is at least one match!")
    print(txt)
else:
    print("No match")



