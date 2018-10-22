for n in range(100, 1000):
    a, b, c = map(int, list(str(n)))
    if a ** 3 + b ** 3 + c ** 3 == n:
        print(n)
