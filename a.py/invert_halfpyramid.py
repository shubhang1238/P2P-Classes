# Invert pryamid
n=int(input("enter the number "))
num=1
for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print("")
