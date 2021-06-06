# Write a Python program to check whether an element exists within a tuple
tuple1 = (5, 3, 2, 8, 4, 4, 6, 2)
n=int(input("enter the word you want to check "))

if n  in tuple1:
    print(n,' is in the tuple', tuple1)
else:
    print(n,'is not in the tuple', tuple1)