# a Python program to remove duplicates from a list
duplicates=[]
n=int(input("enter the no of element in the list  "))
for i in range(n):
    b= int(input())
    duplicates.append(b)
print("list=",duplicates)

print(list(set(duplicates)))