#  Write a Python program to count the occurrences of each word in a given sentence

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('Many of life’s failures are people who did not realize how close they were to success when they gave up '))

