T = int(input())
for tt in range(T):
    n = int(input())
    A = []
    for i in range(n):
        A.append(list(map(int, input().strip().split())))
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            A[i][j] = max(A[i + 1][j] + A[i][j], A[i + 1][j + 1] + A[i][j])
    print(A[0][0])
