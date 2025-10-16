class Solution:
    def nthFibonacci(self, n: int) -> int:
        
        # 1. Handle base cases F(0) and F(1)
        if n == 0:
            return 0
        if n == 1:
            return 1

        # 2. Initialize the first two numbers (a = F(i-2), b = F(i-1))
        # Start with F(0) and F(1)
        a, b = 0, 1
        
        # 3. Iterate from the 2nd number (i=2) up to the nth number
        for i in range(2, n + 1):
            # Calculate the next Fibonacci number (F(i))
            next_fib = a + b
            
            # Shift the window: a becomes the previous F(i-1), b becomes the new F(i)
            a = b
            b = next_fib
            
        # 4. After the loop completes, 'b' holds the nth Fibonacci number F(n)
        return b

# Example Usage to test the Solution class:
solver = Solution()

# Input: n = 5 -> Expected Output: 5 (0, 1, 1, 2, 3, 5)
print(f"F(5) is: {solver.nthFibonacci(5)}") 

# Input: n = 0 -> Expected Output: 0
print(f"F(0) is: {solver.nthFibonacci(0)}")

# Input: n = 1 -> Expected Output: 1
print(f"F(1) is: {solver.nthFibonacci(1)}")

# Input: n = 8 -> Expected Output: 21 (0, 1, 1, 2, 3, 5, 8, 13, 21)
print(f"F(8) is: {solver.nthFibonacci(8)}")
