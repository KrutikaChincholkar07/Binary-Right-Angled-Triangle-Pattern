# Take user input
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # Print 1 if sum of row and column is even, else 0
        print((i + j) % 2, end=" ")
    print()
