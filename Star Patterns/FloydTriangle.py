rows = int(input("Enter the row size for the pattern: "))
j=1
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print(j, end=" ")  # Print numbers
        j+=1
    print()