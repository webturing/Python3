while True:
    A = list(map(int, input().strip().split()))[1:]
    if len(A):
        print(str(sorted(A, key=abs)[::-1])[1:-1].replace(',', ""))
