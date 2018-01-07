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
    result = 0
    if red == 6 and blue == 1:  # 6+1
        result = 1
    elif red == 6 and blue == 0:  # 6+0
        result = 2
    elif red == 5 and blue == 1:
        result = 3
    elif red + blue == 5:
        result = 4
    elif red + blue == 4:
        result = 5
    elif blue == 1:
        result = 6
    return (red, blue, result)


KEY = randomSelect(1, 33, 6) + randomSelect(1, 16, 1)
print(
    "****本期特等奖号码:%02d %02d %02d %02d %02d %02d (%02d)*****" % (KEY[0], KEY[1], KEY[2], KEY[3], KEY[4], KEY[5], KEY[6]))

prizes = [0] * 7
TOTAL = 5000000
PRIZES = [0, 5000000, 100000, 3000, 200, 10, 5, ]
for i in range(TOTAL):
    redBalls = randomSelect(1, 33, 6)
    blueBall = randomSelect(1, 16, 1)
    user = redBalls + blueBall
    red, blue, pr = getPrize(KEY, user)
    prizes[pr] += 1
    if pr in [1, 2, 3, 4]:
        print("User%010d: %d PRIZE (%d+%d)" % (i, pr, red, blue),
              "%02d %02d %02d %02d %02d %02d (%02d)" % (user[0], user[1], user[2], user[3], user[4], user[5], user[6]))
getMoney = sum([prizes[i] * PRIZES[i] for i in range(7)])
print("获奖次数: ", prizes[1:])
print("投入金额: ", TOTAL * 2)
print("获得奖金: ", getMoney)
print("中奖率: %.2f" % (sum(prizes[1:]) * 100 / TOTAL) + "%")
print("返奖率: %.2f" % (getMoney * 100 / (TOTAL * 2)) + "%")
