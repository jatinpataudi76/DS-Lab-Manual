def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)

print("Factorial of 4 =", factorial(4))

# Time complexity : O(n)
# Space complexity : O(n)   (because of recursion stack)