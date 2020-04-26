## The Data
n = 5

## The One-liner
factorial = lambda n: n* factorial(n-1) if n >1 else 1

## The Result

print(factorial(n))
# 120


print(factorial(10))
# 3628800

# Stephen Hawking came up with a concise way to explain recursion: “To understand recursion, one must first understand recursion.”

