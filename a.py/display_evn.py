# Display even Numbers between m and n
m= int (input ("Enter 1st number: ") )
n= int (input ("Enter 2st number: ") )
x=m

if (x%2) != 0:
    x= x+1;
    while x>=m and x<=n:
        print(x)
        x += 2
