for i in range(1000, 10000):
    a, b = i // 100, i % 100
    if (a + b) ** 2 == i:
        print(i, end="\t")
