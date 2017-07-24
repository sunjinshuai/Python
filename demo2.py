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