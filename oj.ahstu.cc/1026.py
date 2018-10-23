a, n = map(int, input().strip().split())
A = [a]
while len(A) < n:
    A.append(A[-1] * 10 + a)
print(sum(A))
