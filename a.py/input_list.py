# Get a list as input from user

lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)