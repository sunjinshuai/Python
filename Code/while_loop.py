# Python 编程中 while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为：
# while 判断条件：
#     执行语句……
# 执行语句可以是单个语句或语句块。判断条件可以是任何表达式，任何非零、或非空（null）的值均为true。
# 当判断条件假false时，循环结束。

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
 
print "Good bye!"

# while 语句时还有另外两个重要的命令 continue，break 来跳过循环，continue 用于跳过该次循环，break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下：
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print i         # 输出双数2、4、6、8、10
 
i = 1
while 1:            # 循环条件为1必定成立
    print i         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

# 无限循环
# var = 1
# while var == 1 :  # 该条件永远为true，循环将无限执行下去
#    num = raw_input("Enter a number  :")
#    print "You entered: ", num
 
# print "Good bye!"

# 注意：以上的无限循环你可以使用 CTRL+C 来中断循环

# 循环使用 else 语句

count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"