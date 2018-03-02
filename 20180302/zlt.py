for a in range(1, 14):
    for b in range(1, 14):
        for c in range(1, 14):
            for d in range(1, 14):
                for e in range(1, 14):
                    for f in range(1, 14):
                        if len(set([a, b, c, d, e, f, 13, 10, 11, 12, 6, 8])) == 12 \
                                and a + 13 + 10 + b == 11 + c + d + 12 == e + 6 + 8 + f \
                                and a + 11 + e == 13 + c + 6 == 10 + d + 8 == b + 12 + f:
                            print(a, b, c, d, e, f)
                            print("-----------------------")
                            print(a, 13, 10, b)
                            print(11, c, d, 12)
                            print(e, 6, 8, f)
                            print("-----------------------")