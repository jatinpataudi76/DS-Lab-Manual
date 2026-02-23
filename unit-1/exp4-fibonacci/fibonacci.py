calls_naive = 0
calls_memo = 0

def fib_naive(n):
    global calls_naive
    calls_naive += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


def fib_memo(n, memo):
    global calls_memo
    calls_memo += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)

    return memo[n]


n = 10

print("Fibonacci =", fib_naive(n))
print("Naive calls =", calls_naive)

memo = {}
print("Fibonacci =", fib_memo(n, memo))
print("Memo calls =", calls_memo)