# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# -*- coding: UTF-8 -*-

d=[]
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if (a != b) and (a != c) and (c != b):
                d.append([a,b,c])
print ("总数量：", len(d))
print (d)

# 计算十进制整数 45678 和十六进制整数 0x12fd2 之和。
print(45678 + 0x12fd2)

# 请用字符串表示出Learn Python in imooc
print("Learn Python in imooc")

# 请计算以下表达式的布尔值（注意==表示判断是否相等）：
# 100 < 99
# 0xff == 255

print(100 < 99)
print(0xff == 255)


print ('The quick brown fox', 'jumps over', 'the lazy dog')

# 请用两种方式打印出 hello, python.
print("hello, python.")
print("hello,","python.")

# 等差数列可以定义为每一项与它的前一项的差等于一个常数，可以用变量 x1 表示等差数列的第一项，用 d 表示公差，请计算数列
# 1 4 7 10 13 16 19 ...
# 前 100 项的和。
# 计算公式 x100 = x1 + (n - 1) * d
# 求和公司 s = (x1 + x100) * n / 2

x1 = 1
d = 3
n = 100
x100 = x1 + (n - 1) * d
s = (x1 + x100) * n / 2
print (s)

# 请将下面两行内容用Python的字符串表示并打印出来：
# Python was started in 1989 by "Guido".
# Python is free and easy to learn.

print("Python was started in 1989 by \"Guido\".")
print("Python is free and easy to learn.")

# raw字符串
print(r"\(~_~)/ \(~_~)/")

# 多行字符串
print('''Line 1
Line 2
Line 3''')

# 请把下面的字符串用r'''...'''的形式改写，并用print打印出来：
# '\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'
print(r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.''')

print (u'''
静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。''')

# 利用while循环计算100以内奇数的和。
sum = 0
x = 1
while x < 100:
    sum = sum + x
    x = x + 2
print (sum)

# 利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
sum = 0
x = 1
n = 1
while True:
    sum = sum + x
    x = x * 2
    n = n + 1
    if n > 20:
        break
print (sum)

# 对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum + x
print (sum)

# 对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print (x * 10 + y)


s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print (s)