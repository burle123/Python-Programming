n=6
for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            if k == 1 or k == 2*i-1 or i== n:
                 print("*", end="")
            else:
                 print(" ", end="")     
        print()