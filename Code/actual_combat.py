#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print i, j, k

# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

x = int(raw_input("净利润："))
if x <= 100000:
    bonus = x * 0.1
    print u"奖金:",bonus,u"元"
elif 100001 < x <= 200000:
    bonus = 10000 + (x - 100000) * 0.075
    print u"奖金:",bonus,u"元"
elif 200001 < x <= 400000:
    bonus = 10000 + 7500 + (x - 200000) * 0.05
    print u"奖金:",bonus,u"元"
elif 400001 < x <= 600000:
    bonus = 10000 + 7500 + 10000 + (x - 400000) * 0.03
    print u"奖金:",bonus,u"元"
elif 600001 < x <= 1000000:
    bonus = 10000 + 7500 + 10000 + 6000 + (x - 600000) * 0.015
    print u"奖金:",bonus,u"元"
elif 600001 < x <= 1000000:
    bonus = 10000 + 7500 + 10000 + 6000 + 6000 + (x - 600000) * 0.01
    print u"奖金:",bonus,u"元"

# 题目：列表转换为字典。

k = [1, 2, 3, 4] # key
v = ['a', 'b', 'c', 'd']

d = {}

for i in range(len(v)):
    d.setdefault(v[i], k[i])
print d

# 题目：将一个列表的数据复制到另一个列表中。

l1 = [1, 2, 3, 4]
l2 = []

for i in range(len(l1)):
    l2.append(i+1)

print l2

# 题目：计算字符串中子串出现的次数。
str = "adfjladfjla;sdfasdfasfkl"
sub = "ad"

print str.count(sub)