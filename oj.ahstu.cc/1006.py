import re


def check(s):
    w = s.split('.')
    if len(w) != 4:
        return False
    for e in w:
        if not re.match(r'\d+', e) or int(e) > 255 or int(e) < 0:
            return False
    return True


while True:
    if check(input().strip()):
        print('Y')
    else:
        print('N')
