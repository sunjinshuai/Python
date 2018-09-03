var1 = 'Hello World!'
var2 = "Python Runoob"

print var1,var2

# Python字符串运算符

# +	字符串连接	
# *	重复输出字符串	
# [] 通过索引获取字符串中字符	
# [ : ]	截取字符串中的一部分	
# in	成员运算符 - 如果字符串中包含给定的字符返回 True
# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	>>>"M" not in a True
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	

a = "Hello"
b = "Python"
print a + b
print a * 2 
print a[1]
print b[1:3]
if( "H" in a) :
    print "H 在变量 a 中" 
else :
    print "H 不在变量 a 中" 
 
if( "M" not in a) :
    print "M 不在变量 a 中" 
else :
    print "M 在变量 a 中"
 
print r"\n"
print R"\n"

# Python 字符串格式化
# %c	 格式化字符及其ASCII码
# %s	 格式化字符串
# %d	 格式化整数
# %u	 格式化无符号整型
# %o	 格式化无符号八进制数
# %x	 格式化无符号十六进制数
# %X	 格式化无符号十六进制数（大写）
# %f	 格式化浮点数字，可指定小数点后的精度
# %e	 用科学计数法格式化浮点数
# %E	 作用同%e，用科学计数法格式化浮点数
# %g	 %f和%e的简写
# %G	 %f 和 %E 的简写
# %p	 用十六进制数格式化变量的地址

print "My name is %s and weight is %d kg!" % ('Zara', 21) 

# Python三引号（triple quotes）

# python中三引号可以将复杂的字符串进行复制:
# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
# 三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。

hi = '''hi 
there'''
print hi

# Python capitalize()将字符串的第一个字母变成大写,其他字母变小写
# 该方法返回一个首字母大写的字符串。

s = 'a, B'
print s

# Python center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
# center()方法语法：
# str.center(width[, fillchar])
# width -- 字符串的总宽度。
# fillchar -- 填充字符。
# 该方法返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。

str = "Hello"
print str.center(20, "*")

# Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
# count()方法语法：
# str.count(sub, start= 0,end=len(string))
# sub -- 搜索的子字符串
# start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
# end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
# 该方法返回子字符串在字符串中出现的次数

str = "this is string example....wow!!!";
sub = "t"
print str.count(sub,0,len(str))

# Python decode() 方法以 encoding 指定的编码格式解码字符串。默认编码为字符串编码。
# decode()方法语法：
# str.decode(encoding='UTF-8',errors='strict')
# encoding -- 要使用的编码，如"UTF-8"。
# errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
# 该方法返回解码后的字符串。

# Python encode() 方法以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
# encode()方法语法：
# str.encode(encoding='UTF-8',errors='strict')
# encoding -- 要使用的编码，如"UTF-8"。
# errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
# 该方法返回编码后的字符串。

str = "this is string example....wow!!!";
str = str.encode('base64','strict');
 
print "Encoded String: " + str;
print "Decoded String: " + str.decode('base64','strict')

# Python endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
# endswith()方法语法：
# str.endswith(suffix[, start[, end]])
# suffix -- 该参数可以是一个字符串或者是一个元素。
# start -- 字符串中的开始位置。
# end -- 字符中结束位置。
# 如果字符串含有指定的后缀返回True，否则返回False。

str = "this is string example....wow!!!";
suffix = "wow!!!";
print str.endswith(suffix)
print str.endswith(suffix, 10, 20);

# Python expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
# expandtabs()方法语法：
# str.expandtabs(tabsize=8)
# tabsize -- 指定转换字符串中的 tab 符号('\t')转为空格的字符数。
# 该方法返回字符串中的 tab 符号('\t')转为空格后生成的新字符串。

str = "this is\tstring example....wow!!!";

print "Original string: " + str;
print "Defualt exapanded tab: " +  str.expandtabs();
print "Double exapanded tab: " +  str.expandtabs(16);

# Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
# find()方法语法：
# str.find(str, beg=0, end=len(string))
# str -- 指定检索的字符串
# beg -- 开始索引，默认为0。
# end -- 结束索引，默认为字符串的长度。
# 如果包含子字符串返回开始的索引值，否则返回-1。

str1 = "this is string example....wow!!!";
str2 = "exam";
 
print str1.find(str2);
print str1.find(str2, 10);
print str1.find(str2, 40);

# Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
# 基本语法是通过 {} 和 : 来代替以前的 % 。
# format 函数可以接受不限个参数，位置可以不按顺序。

print "{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
print "{0} {1}".format("hello", "world")  # 设置指定位置
print "{1} {0} {1}".format("hello", "world")  # 设置指定位置

# Python index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
# index()方法语法：
# str.index(str, beg=0, end=len(string))
# str -- 指定检索的字符串
# beg -- 开始索引，默认为0。
# end -- 结束索引，默认为字符串的长度。
# 如果包含子字符串返回开始的索引值，否则抛出异常。

str1 = "this is string example....wow!!!";
str2 = "exam";
 
print str1.index(str2);
print str1.index(str2, 10);
print str1.index(str2, 40);

# Python isalnum() 方法检测字符串是否由字母和数字组成。
# isalnum()方法语法：
# str.isalnum()
# 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False

str = "this2009";  # 字符中没有空格
print str.isalnum();
 
str = "this is string example....wow!!!";
print str.isalnum();

# Python isalpha() 方法检测字符串是否只由字母组成。
# isalpha()方法语法：
# str.isalpha()
# 如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

str = "this";  # No space & digit in this string
print str.isalpha();

str = "this is string example....wow!!!";
print str.isalpha();

# Python istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
# istitle()方法语法：
# str.istitle()
# 如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False.

str = "This Is String Example...Wow!!!";
print str.istitle();

str = "This is string example....wow!!!";
print str.istitle();

# Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# join()方法语法：
# str.join(sequence)
# sequence -- 要连接的元素序列。
# 返回通过指定字符连接序列中元素后生成的新字符串。

str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );