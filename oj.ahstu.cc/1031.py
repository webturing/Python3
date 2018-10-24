a = 95859
while True:
    a += 2
    if str(a) == str(a)[::-1]:
        print(a)
        break
