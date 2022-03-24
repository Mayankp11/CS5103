def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
val = input("Enter your Words: ")
print(word_count(val))


jdshfksjdhfksjdfhskjfhs