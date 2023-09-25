rows = int(input("Enter number of rows: "))
j=0
for i in range(rows):
    for j in range(i+2):
        print(j*2, end=" ")
    print("\n")
