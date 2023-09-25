rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+2):
    for j in range(1, i):
        print(number, end=" ")
        number += 1
    print()