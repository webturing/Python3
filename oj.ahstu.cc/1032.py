N = 100
for cock in range(N + 1):
    for hen in range(N + 1 - cock):
        chicken = N - cock - hen
        if cock * 5 + hen * 3 + chicken / 3 == N:
            print("cock=%d,hen=%d,chicken=%d" % (cock, hen, chicken))
