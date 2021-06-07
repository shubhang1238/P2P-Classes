print("\nfull hollow pyramid:")
row6=int(input("enter the no. of rows"))
i,k=1,2
for row in range(1,row6+1):
    for col in range(1,2*row6):
        if(row+col==row6+1):
            print("1",end=" ")
        elif(row==row6 and col!=k):
            print(col-i,end=" ")
            k=k+2
            i=i+1
        elif(col-row==row6-1):
            print(row,end=" ")
        else:
            print(" ",end=" ")
    print()