import math
while True:
    x1, y1, x2, y2 = map(float, input().strip().split())
    print("%.2f" % math.hypot(x1 - x2, y1 - y2))
