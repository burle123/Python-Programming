rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, rows + 1):  # Inner loop for columns
#         print(j, end=" ")  # Print numbers
#     print()

for i in range(5, 0,-1):  # Outer loop for rows
    for j in range(5, 0,-1):  # Inner loop for columns
        print(j, end=" ")  # Print numbers
    print()