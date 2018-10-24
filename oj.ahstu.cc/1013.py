f = lambda n: sum(list(filter(lambda x: n % x == 0, range(1, n))))
for a in range(1, 3001):
    b = f(a)
    if b > a == f(b):
        print('(%d,%d)' % (a, b), end='')
