n = int(input())
print("%d*%d*%d" % (n, n, n), end="=")
print(n ** 3, end="=")
for e in range(n * n - n + 1, n * n - n - 1 + 2 * n, 2):
    print(e, end="+")
print(n * n + n - 1)
