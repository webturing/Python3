for e in list(filter(lambda n: (n // 100) ** 3 + (n % 100 // 10) ** 3 + (n % 10) ** 3 == n, range(100, 1000))):
    print(e, end="  ")
