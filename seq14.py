rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("python", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("python", end=' ')
    print("\r")








word = "Python"
x = ""
for i in word:
    x += i
    print(x)
for i in word:
    x- i
    print(x)