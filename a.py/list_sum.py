# Find sum and average of List in Python
List=[ 1,24.5,51,55,8,54,73,24,8]
count = 0
for i in List:
    count += i
    avg = count/len(List)
print("sum  = ", count)
print("average = ", avg)
