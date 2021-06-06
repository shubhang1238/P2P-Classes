# Python program to print even length words in a string
s = "Welcome to the World of programming"
# split the string
s = s.split(' ')
print("the string with the even no of words are")
for word in s:

    if len(word)%2==0:
        print(word) 