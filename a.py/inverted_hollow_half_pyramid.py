
print("\ninverted half pyramid:")
row5=int(input("enter no. of rows:"))
for row in range(1,row5+1):
    for col in range(1,row5+1):
        if(row==1) :
            print(col,end=" ")
        elif(col==1):
            print(row,end=" ")
        elif(row+col==(row5+1)):
            print(row5,end=" ")
        else:
            print(" ",end=" ")
    print()
