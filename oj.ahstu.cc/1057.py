x, y = map(int, input().strip().split())
print(sum(filter(lambda x: x % 3 == 1 and x % 5 == 3, range(x, 1 + y))))
