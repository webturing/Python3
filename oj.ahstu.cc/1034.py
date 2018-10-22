import math


def prime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for c in range(3, int(math.sqrt(n) + 1)):
        if n % c == 0:
            return False
    return True


n = int(input().strip())
if prime(n):
    print(1)
else:
    print(0)
