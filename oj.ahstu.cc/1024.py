def factorial(n):
    if n <= 1: return 1
    return factorial(n - 1) * n;


n = int(input())
print(sum(map(factorial, range(1, n + 1))))
