rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+2):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 2
    print()