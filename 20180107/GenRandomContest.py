MIN_PROBLEM_ID, MAX_PROBLEM_ID = 1000, 2516

import random


def genRandomContest(number=8):
    problems = list(range(MIN_PROBLEM_ID, MAX_PROBLEM_ID + 1))
    random.shuffle(problems)
    return sorted(problems[0:number])


print(genRandomContest())
print(genRandomContest(16))
