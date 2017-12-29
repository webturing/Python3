import string
dic=dict()
for line in open('Test.py'):
    print(line,end='')
    for char in line:
        if  char in string.ascii_letters:
            if char in dic:
                dic[char]+=1
            else:
                dic[char]=1
print(dic)
