
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)

print('Tuple : ',tuple)

print(tuple)
n=int(input("enter the number to count  "))

count = tuple.count(n)
print(count)