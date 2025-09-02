# Python Loops Theory

# 1. For Loop
# Used to iterate over a sequence (list, tuple, string, etc.)

for i in range(5):
    print("For loop iteration:", i)

# 2. While Loop
# Repeats as long as a condition is True

count = 0
while count < 5:
    print("While loop count:", count)
    count += 1

# 3. Loop Control Statements
# break: Exit the loop early
# continue: Skip to the next iteration
# pass: Do nothing (placeholder)

for i in range(5):
    if i == 2:
        continue  # Skip when i == 2
    if i == 4:
        break     # Exit loop when i == 4
    print("Control statement example:", i)

# 4. Nested Loops
# Loops inside loops

for i in range(2):
    for j in range(3):
        print(f"Nested loop: i={i}, j={j}")

# 5. else with Loops
# The else block runs if the loop completes normally (not broken)

for i in range(3):
    print("Loop with else:", i)
else:
    print("Loop completed without break.")
    