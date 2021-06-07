# full pyramid
print("\tfull pyramid:")
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for space in range(1,n-i+1):
        print(" ",end=" ")
    k=i
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    k=k-2
    for j in range(1,i):
        print(k,end=" ")
        k-=1
    print()
