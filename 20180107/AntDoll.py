"""
蚂蚁周周乐模拟
规则52张扑克牌，随机抽4张
用户随机抽4张
如果4张完全相同则1等奖4999元
连续3张相同则2等奖88元
连续2张相同则3等奖2元
同顺序1张相同则4等奖奖金周周乐一注
"""

import random

KIND = "♧ ♢ ♠ ♡".split()
DIGIT = "A_ 2_ 3_ 4_ 5_ 6_ 7_ 8_ 9_ 10 J_ Q_ K_".split()
# print(KIND)
# print(DIGIT)

CARDS = []
for i in range(52):
    CARDS += [KIND[i // 13] + DIGIT[i % 13]]
CARDS += ["x王", "D王"]
print(CARDS)


def randomSelect(begin, end, number):
    problems = list(range(begin, end + 1))
    random.shuffle(problems)
    return problems[0:number]


def pretty(arr):
    s = ""
    for i in range(4):
        s += "[" + CARDS[arr[i]] + "] "
    return s


def getPrize(user, key):
    if key == user:
        return 1
    if key[0:3] in [user[0:3], user[1:4]] or key[1:4] in [user[0:3], user[1:4]]:
        return 2
    if key[0:2] in [user[0:2], user[1:3], user[2:4]] or key[1:3] in [user[0:2], user[1:3], user[2:4]] or key[2:4] in [
        user[0:2], user[1:3], user[2:4]]:
        return 3
    tot = 0
    for i in range(4):
        if key[i] == user[i]:
            tot += 1
    if tot > 0:
        return 4
    return 0


KEY = randomSelect(0, 53, 4)
print("*" * 8 + pretty(KEY) + "*" * 8)

prize = [0] * 5
total = 1000000
for i in range(total):
    user = randomSelect(1, 52, 4)
    #    print(pretty(user))
    pr = getPrize(KEY, user)
    prize[pr] += 1
    if pr in [1, 2]:
        print("%07d" % i, pretty(user), pr)
total -= prize[4]
print(prize[1:])
print("TOTAL", total)
print("总金额:", prize[1] * 4999 + prize[2] * 88 + prize[3] * 2)
