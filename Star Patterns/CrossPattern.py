rows = int(input("Enter the row size for the pattern:"))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        if i == j or i + j == rows + 1:  # Print stars in cross pattern
            print("*", end=" ")
        else:
            print(" ", end=" ")  # Print space
    print()