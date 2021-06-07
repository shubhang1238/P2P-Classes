print("\nhollow half pyramid:")
row4=int(input("enter no. of rows:"))
for row in range(1,row4+1):
    for col in range(1,row4+1):
        if(col==1 or row==row4 or row==col):
            print(col,end=" ")
        else:
            print(end="  ")
    print()
