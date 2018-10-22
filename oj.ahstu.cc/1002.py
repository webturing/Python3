import math

a, b, c = map(float, input().strip().split())
delta = math.sqrt(b ** 2 - 4 * a * c)
x1, x2 = (-b - delta) / (2 * a), (-b + delta) / (2 * a)
if x1 < x2:
    x1, x2 = x2, x1
print("%.2f %.2f" % (x1, x2))
