# 数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。

# 以下实例在变量赋值时 Number 对象将被创建：

var1 = 1
var2 = 10

var1 = "可以改变"

# 注意：可以使用del语句删除一些 Number 对象引用。

# del var1
# File "/Users/sunjinshuai/Desktop/Python/number.py", line 12, in <module>
    # print var1
# NameError: name 'var1' is not defined

print var1

# Python 支持四种不同的数值类型：
# 整型(Int)                           - 通常被称为是整型或整数，是正或负整数，不带小数点。
# 长整型(long integers)               - 无限大小的整数，整数最后是一个大写或小写的L。
# 浮点型(floating point real values)  - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
# 复数(complex numbers)               - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

# Python Number 类型转换

# int(x [,base ])         将x转换为一个整数  
# long(x [,base ])        将x转换为一个长整数  
# float(x )               将x转换到一个浮点数  
# complex(real [,imag ])  创建一个复数  
# str(x )                 将对象 x 转换为字符串  
# repr(x )                将对象 x 转换为表达式字符串  
# eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
# tuple(s )               将序列 s 转换为一个元组  
# list(s )                将序列 s 转换为一个列表  
# chr(x )                 将一个整数转换为一个字符  
# unichr(x )              将一个整数转换为Unicode字符  
# ord(x )                 将一个字符转换为它的整数值  
# hex(x )                 将一个整数转换为一个十六进制字符串  
# oct(x )                 将一个整数转换为一个八进制字符串  