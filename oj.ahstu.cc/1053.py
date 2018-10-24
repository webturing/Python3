G = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789 ~!@#$%^".split()


def check(p):
    if not 8 <= len(p) <= 16: return False
    cnt = 0
    for g in G:
        for char in p:
            if char in g:
                cnt += 1
                break
    return cnt >= 3


T = int(input())
for tt in range(T):
    if check(input()):
        print("YES")
    else:
        print("NO")
