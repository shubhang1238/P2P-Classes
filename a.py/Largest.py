# find the largest Among the three numbers
a=int(input("enter the 1st no  "))
b=int(input("enter the 2nd no  " ))
c=int(input("enter the 3rd no  " ))
if a>b and a>c:
    print(a,"is the larget no among three")
elif b>a and b>c:
    print(b,"is the larget no among three")
else:
    print(c,"is the larget no among three")