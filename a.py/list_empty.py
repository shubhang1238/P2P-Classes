# Write a Python program to check a list is empty or not

lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)
if not lst:
      print("List is empty")
else:
     print("List is not empty")