n = int(input())
if n==1:
    print(1)
else:
    A = [1, 1]
    while len(A) < n:
        A.append(A[-1] + A[-2])
    print(str(A)[1:-1].replace(',',''))
