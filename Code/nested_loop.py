# Python 语言允许在一个循环体里面嵌入另一个循环。
# Python for 循环嵌套语法：
# for iterating_var in sequence:
#    for iterating_var in sequence:
#       statements(s)
#    statements(s)

# Python while 循环嵌套语法：
# while expression:
#    while expression:
#       statement(s)
#    statement(s)

# 以下实例使用了嵌套循环输出2~100之间的素数：

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " 是素数"
   i = i + 1
 
print "Good bye!"