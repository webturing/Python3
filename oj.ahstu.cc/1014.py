def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = 40
for e in list(filter(lambda x: gcd(x, n) == 1, range(1, n))):
    print('%d/%d' % (e, n), end=',')
