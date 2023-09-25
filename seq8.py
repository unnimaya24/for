rows = int(input("Enter number of rows: "))
number = 2

for i in range(1, rows+3):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 2
    print()