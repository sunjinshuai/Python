# 变量赋值
# Python 中的变量赋值不需要类型声明。
# 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
# 每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 等号（=）用来给变量赋值。
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
 
print counter
print miles
print name

# 多个变量赋值
# Python允许你同时为多个变量赋值。例如：
a = b = c = 1
print a
print b
print c

# 也可以为多个对象指定多个变量。例如：
d, e, f = 1, 2, "john"
print d
print e
print f