import random


def randomSelect(begin, end, number):
    problems = list(range(begin, end + 1))
    random.shuffle(problems)
    return problems[0:number]


def getPrize(key, user):
    red, blue = 0, 0
    for i in range(6):
        if key[i] == user[i]:
            red += 1
    if key[-1] == user[-1]:
        blue += 1
    if red == 6 and blue == 1:  # 6+1
        return 1
    if red == 6 and blue == 0:  # 6+0
        return 2
    if red == 5 and blue == 1:
        return 3
    if red + blue == 5:
        return 4
    if red + blue == 4:
        return 5
    if blue == 1:
        return 6
    return 0


KEY = randomSelect(1, 33, 6) + randomSelect(1, 16, 1)
print("本期特等奖号码:", KEY[0:6], "(", KEY[-1], ")")

prizes = [0] * 7
TOTAL = 500000
PRIZES = [0, 5000000, 100000, 3000, 200, 10, 5, ]
for i in range(TOTAL):
    redBalls = randomSelect(1, 33, 6)
    blueBall = randomSelect(1, 16, 1)
    user = redBalls + blueBall
    prizes[getPrize(KEY, user)] += 1
getMoney = sum([prizes[i] * PRIZES[i] for i in range(7)])
print("获奖次数: ", prizes[1:])
print("投入金额: ", TOTAL * 2)
print("获得奖金: ", getMoney)
print("中奖率: %.2f" % (sum(prizes[1:]) * 100 / TOTAL) + "%")
print("返奖率: %.2f" % (getMoney * 100 / (TOTAL * 2)) + "%")
