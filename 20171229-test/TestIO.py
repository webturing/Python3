import string

dic = dict()
for line in open('TestIO.py'):
    for char in line:
        if char in string.ascii_letters:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
print(dic)  # DEBUG

for k in string.ascii_lowercase:
    if k not in dic:
        dic[k] = 0
    print(k, '#' * dic[k])
