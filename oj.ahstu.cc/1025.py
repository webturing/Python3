import math

n = int(input())
print(list(map(lambda x: 1 /x**2, range(1, n + 1))))
s = sum(map(lambda x: 1 /x**2, range(1, n + 1)))
print("%.6f" % (math.sqrt(6 * s)))
