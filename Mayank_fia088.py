import re
#function for unique word count in the string
def uniqueWordCout(fileContent):
    uniqueWordDictionary = {}
    words = filter(None, re.split(' |\n|\t', fileContent))
    for word in words:
        uniqueWordDictionary[word] = uniqueWordDictionary.get(word, 0) + 1
    return uniqueWordDictionary
# function used for replacement
   
def replaceWord(fileContent, findBy, replaceBy):
    return re.sub('[ \t\n]'+findBy+'[ \t\n]', lambda x : x.group().replace(findBy, replaceBy), fileContent)

#replacing the words present in the string

inputFile = (open('C:/Users/mayan/Documents/CS_5103_fia088/sample.txt'))
x = inputFile.read()

y = uniqueWordCout(x)


print(" \n Frequency of each word is : \n")
for key in y:
    
    print("\t",key, '->', y[key])

print("\n")
print("unique word count = ",uniqueWordCout(x))
print("\n")
print("Original text message= ",x)
print("\n")



existing_word = input("Enter the word in the string : ")
replace_word = input("\nEnter the word to be replaced with : ")
print("\n")

print("After replacing text message =",replaceWord(x,existing_word ,replace_word))