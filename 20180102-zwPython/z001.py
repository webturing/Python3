# -*- coding: utf-8 -*-
import arrow
import pypinyin

print("hello,ziwang.com")
print(arrow.__version__)
print(pypinyin.__version__)
t0 = arrow.now()
t2 = t0.shift(days=-2)
print(t0)
print(t2)
print(pypinyin.pinyin('中心'))
