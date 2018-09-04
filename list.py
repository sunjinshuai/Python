list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

print list1, list2, list3

# 访问列表中的值
# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

# 更新列表
# 你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项，如下所示：

list = []               ## 空列表
list.append('Google')   ## 使用 append() 添加元素
list.append('Python')
print list

# 删除列表元素
# 可以使用 del 语句来删除列表的元素，如下实例：

list1 = ['Python', 'iOS', 'Java', 'C++']
 
print list1
del list1[2]
print "After deleting value at index 2 : "
print list1

# Python列表脚本操作符
# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。

list1 = ['Python', 'iOS', 'Java', 'C++']
print len(list1)
list2 = ['C', 'Ruby', 'Javastript']
print list1 + list2
print ['Python'] * 4

print 'iOS' in list1

for str in list1:
    print str

# Python列表截取
list1 = ['Python', 'iOS', 'Java', 'C++']
print list1[2]
print list1[-2]
print list1[1:]

# cmp() 方法用于比较两个列表的元素。
# cmp()方法语法：
# cmp(list1, list2)

# 如果比较的元素是同类型的,则比较其值,返回结果。
# 如果两个元素不是同一种类型,则检查它们是否是数字。

    # 如果是数字,执行必要的数字强制类型转换,然后比较。
    # 如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的")
    # 否则,通过类型名字的字母顺序进行比较。
# 如果有一个列表首先到达末尾,则另一个长一点的列表"大"。
# 如果我们用尽了两个列表的元素而且所 有元素都是相等的,那么结果就是个平局,就是说返回一个 0。

list1, list2 = [123, 'xyz'], [456, 'abc']

print cmp(list1, list2);
print cmp(list2, list1);
list3 = list2 + [786];
list4 = [123, 'xyz']
print cmp(list2, list3)
print cmp(list1, list4)

# extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
# extend()方法语法：
# list.extend(seq)
# 该方法没有返回值，但会在已存在的列表中添加新的列表内容。

aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print "Extended List : ", aList