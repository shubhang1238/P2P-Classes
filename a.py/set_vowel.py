# Python program to count number of vowels using sets in given string

str = "Welcome to the World of Programming"
count = 0

vowel = set("aeiouAEIOU")

for alphabet in str:

    if alphabet in vowel:
        count = count + 1

print("No. of vowels :", count)

