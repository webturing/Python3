def f(x):
    if x == 1:
        return 10
    return f(x - 1) + 2


print(f(int(input())))
