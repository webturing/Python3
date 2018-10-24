def ok(n):
    m = n * n
    s, t = map(str, (n, m))
    return t.endswith(s)


print(str(list(filter(ok, range(200000))))[1:-1].replace(',', ' '))
