rows = int(input("Enter number of rows: "))
j=1
for i in range(rows):
    for j in range(i+1):
       print((j * 2-1), end=" ")
       
    print("\n")

