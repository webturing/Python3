# coding=utf-8
# 1.    随机产生一些1—100之间的整数，直到产生的数为50为止。
import random


def p01(start, end, target):
    a, tot = random.randint(start, end), 0
    while a != target:
        print(a, end=' ')
        a, tot = random.randint(start, end), tot + 1
    print("\n" + str(tot))


p01(1, 100, 50)


# 2计算1—1000之间能同时被3和5整除的整数的和。
def r_sum(start, end, mod):
    end, start = end // mod * mod, (start + mod - 1) // mod * mod
    return (start + end) * ((end - start) / mod + 1) / 2;


print(int(r_sum(1, 1000, 15)))


# 3.    打印数字图形：
def printTriangle(n):
    for i in range(n + 1):
        print("  " * (n - i), end=' ')
        for j in range(i + 1):
            print(j + 1, end=' ')
        for j in range(i):
            print(i - j, end=' ')
        print()
    for i in range(n):
        print("  " * (i + 1), end=' ')
        for j in range(n - i):
            print(j + 1, end=' ')
        for j in range(n - i - 1):
            print(n - i - j - 1, end=' ')
        print()


printTriangle(4)
# 4.    一百匹马驮一百块瓦，一匹大马可以驮3块，一匹母马可驮2块，小马2匹可驮1块。试编程求需要各种马多少匹？
x, y, z = 0, 0, 0
for x in range(0, 101):
    for y in range(0, 100 - x + 1):
        z = 100 - x - y
        if 3 * x + 2 * y + z / 2 == 100:
            print("%2d %2d %2d" % (x, y, z))
            # 5.有三种纪念邮票，第一种每套一张售价2元，第二种每套一张售价4元，第三种每套9张售价2元。现用100元买了100张邮票，问这三种邮票各买几张？
a, b, c = 0, 0, 0
for a in range(0, 101):
    for b in range(0, 101 - a):
        c = 100 - a - b
        if 2 * a + b * 4 + c / 9 == 100:
            print(("%d %d %d ") % (a, b, c))
'''
赵、钱、孙、李、周五人围着一张圆桌吃饭。饭后，周回忆说：“吃饭时，赵坐在钱旁边，钱的左边是孙或李”；李回忆说：“钱坐在孙左边，我挨着孙坐”。
结果他们一句也没有说对。请问，他们在怎样坐的？   
'''


def left(a, b):
    return a + 1 == b or a == 5 and b == 1


def right(a, b):
    return left(b, a)


def adj(a, b):
    return right(a, b) or left(a, b)


zhao, qian, sun, li, zhou = 1, 1, 1, 1, 1
for qian in range(2, 6):
    for sun in range(2, 6):
        if sun == qian: continue
        for li in range(2, 6):
            if li == qian or li == sun:
                continue
            zhou = 15 - zhao - qian - sun - li
            if adj(zhao, qian) or left(qian, sun) or left(qian, li):
                continue
            if left(sun, qian) or adj(sun, li):
                continue
            print("%d %d %d %d %d" % (zhao, qian, sun, li, zhou))
'''
7. 找数。一个三位数，各位数字互不相同，十位数字比个位、百位数字之和还要大，且十位、百位数字之和不是质数。编程找出所有符合条件的三位数。   
注：1.   不能手算后直接打印结果。   
'''
import math


def prime(n):
    for c in range(2, int(math.sqrt(n))):
        if n % c == 0:
            return False
    return True


for n in range(100, 1000):
    a, b, c = n // 100, (n % 100) // 10, n % 10
    if a == b or b == c or c == a or b <= a + c or prime(b + c):
        continue
    print(n, end=" ")
'''
8.    选人。一个小组共五人，分别为A、B、C、D、E。现有一项任务，要他们中的3个人去完成。
已知：
（1）A、C不能都去；
（2）B、C不能都不去；
（3）如果C去了，D、E就只能去一个，且必须去一个；
（4）B、C、D不能都去；
（5）如果B去了，D、E就不能都去。编程找出此项任务该由哪三人去完成的所有组合。   
'''
a, b, c, d, e = 0, 0, 0, 0, 0
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                for e in range(0, 2):
                    if a == 1 and c == 1: continue
                    if b == 0 and c == 0: continue
                    if c == 1 and d + e != 1: continue
                    if b == 1 and c == 1 and d == 1: continue
                    if b == 1 and d == 1 and d == 1: continue
                    if a + b + c + d + e == 3:
                        print(a, b, c, d, e)

# 9.     输入一个字符串，内有数字和非数字字符。如A123X456Y7A，302ATB567BC，打印字符串中所有连续（指不含非数字字符）的数字所组成的整数，并统计共有多少个整数。
import re

s = "A123X456Y7A，302ATB567BC"
print(re.split('\\D+', s))
# 10.A、B、C三人进入决赛，赛前A说：“B和C得第二，我得第一”；B说：“我进入前两名，丙得第三名”；C说：“A不是第二，B不是第一”。比赛产生了一、二、三名，比赛结果显示：获得第一的选手全说对了，获得第二的选手说对了一句，获得第三的选手全说错了。编程求出A、B、C三名选手的名次。
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            if a == b or b == c or c == a:
                continue
            pa, pb, pc = 0, 0, 0
            if b == 2 and c == 2:
                pa += 1
            if a == 1:
                pa += 1
            if b <= 2:
                pb += 1
            if c == 3:
                pb += 1
            if a != 2:
                pc += 1
            if b != 1:
                pc += 1
            if a + pa == b + pb and b + pb == c + pc:
                print(a, b, c)
                # 11 甲、乙、丙、丁四人共有糖若干块，甲先拿出一些糖分给另外三人，使他们三人的糖数加倍；乙拿出一些糖分给另外三人，也使他们三人的糖数加倍；丙、丁也照此办理，此时甲、乙、丙、丁四人各有16块，编程求出四个人开始各有糖多少块。
'''
11.    甲、乙、丙、丁四人共有糖若干块，
甲先拿出一些糖分给另外三人，使他们三人的糖数加倍；
乙拿出一些糖分给另外三人，也使他们三人的糖数加倍；
丙、丁也照此办理，此时甲、乙、丙、丁四人各有16块，
编程求出四个人开始各有糖多少块。  
'''


def solve(n):
    a, b, c, d = 0, 0, 0, 0
    for a in range(n // 2, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                d = n - a - b - c
                ca, cb, cc, cd = a, b, c, d
                ca, cb, cc, cd = ca - cb - cc - cd, 2 * cb, 2 * cc, 2 * cd
                cb, cc, cd, ca = cb - cc - cd - ca, 2 * cc, 2 * cd, 2 * ca
                cc, cd, ca, cb = cc - cd - ca - cb, 2 * cd, 2 * ca, 2 * cb
                cd, ca, cb, cc = cd - ca - cb - cc, 2 * ca, 2 * cb, 2 * cc
                if ca == n / 4 and cb == n / 4 and cc == n / 4 and cd == n / 4:
                    print(a, b, c, d)
                    # 以下验证一下
                    ca, cb, cc, cd = a, b, c, d
                    ca, cb, cc, cd = ca - cb - cc - cd, 2 * cb, 2 * cc, 2 * cd
                    print(ca, cb, cc, cd)
                    cb, cc, cd, ca = cb - cc - cd - ca, 2 * cc, 2 * cd, 2 * ca
                    print(ca, cb, cc, cd)
                    cc, cd, ca, cb = cc - cd - ca - cb, 2 * cd, 2 * ca, 2 * cb
                    print(ca, cb, cc, cd)
                    cd, ca, cb, cc = cd - ca - cb - cc, 2 * ca, 2 * cb, 2 * cc
                    print(ca, cb, cc, cd)


solve(64)

'''
12.    截数问题:   任意一个自然数，我们可以将其平均截取成三个自然数。例如自然数135768，可以截取成13,57,68三个自然数。
如果某自然数不能平均截取(位数不能被3整除)，可将该自然数高位补零后截取。现编程从键盘上输入一个自然数N(N的位数<12)，
计算截取后第一个数加第三个数减第二个数的结果。
'''


def solve(s):
    while len(s) % 3 != 0:
        s = "0" + s
    n = len(s) // 3
    a = int(s[0:n])
    b = int(s[n:2 * n])
    c = int(s[2 * n:3 * n])
    print(a + c - b)


solve("1234567")
