# -*- coding: UTF-8 -*-

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：

# d = {key1 : value1, key2 : value2 }

# 注意：键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。

dict = {'a': 1, 'b': 2, 'b': '3'};
print dict['b']

print dict

# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print "dict['Name']: ", dict['Name'];
print "dict['Age']: ", dict['Age'];

# 如果用字典里没有的键访问数据，会输出错误如下：
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
 
# print "dict['Alice']: ", dict['Alice'];

# Traceback (most recent call last):
#   File "test.py", line 5, in <module>
#     print "dict['Alice']: ", dict['Alice'];
# KeyError: 'Alice'

# 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];

# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作。
# 显示删除一个字典用del命令，如下实例：
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
del dict['Name']; # 删除键是'Name'的条目
print dict

dict.clear();     # 清空词典所有条目
print dict

del dict ;        # 删除词典
print dict

# print "dict['Age']: ", dict['Age'];
# dict['Age']:  Traceback (most recent call last):
#   File "/Users/sunjinshuai/Desktop/Python/dictionary.py", line 51, in <module>
#     print "dict['Age']: ", dict['Age'];
# TypeError: 'type' object has no attribute '__getitem__'

# 字典键的特性
# 字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被覆盖，如下实例：
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};
 
print "dict['Name']: ", dict['Name'];

# 2）键必须不可变，所以可以用数字，字符串或元组充当，但是用列表就不行，如下实例：

# list = ['Name']
# dict = {list: 'Zara', 'Age': 7};
 
# print "dict['Name']: ", dict[list];
# Traceback (most recent call last):
#   File "/Users/sunjinshuai/Desktop/Python/dictionary.py", line 68, in <module>
#     dict = {['Name']: 'Zara', 'Age': 7};
# TypeError: unhashable type: 'list'

tup = (1, 2, 3, 4, 5 )
dict = {tup: 'Zara', 'Age': 7};
print "dict['Name']: ", dict[tup];

# Python 字典的 cmp() 函数用于比较两个字典元素。
# cmp()方法语法：
# cmp(dict1, dict2)
# dict1 -- 比较的字典。
# dict2 -- 比较的字典。
# 如果两个字典的元素相同返回0，如果字典dict1大于字典dict2返回1，如果字典dict1小于字典dict2返回-1。

dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = {'Name': 'Mahnaz', 'Age': 27};
dict3 = {'Name': 'Abid', 'Age': 27};
dict4 = {'Name': 'Zara', 'Age': 7};
print "Return Value : %d" %  cmp (dict1, dict2)
print "Return Value : %d" %  cmp (dict2, dict3)
print "Return Value : %d" %  cmp (dict1, dict4)

# Python 字典 popitem() 方法随机返回并删除字典中的一对键和值。
# 如果字典已经为空，却调用了此方法，就报出KeyError异常。
# 返回一个键值对(key,value)形式。

site = {'name': 'python', 'alexa': 10000, 'url': 'www.baidu.com'}
pop_obj = site.popitem()
# print(pop_obj)
# print(site)

# Python 字典 pop() 方法删除字典给定键 key 及对应的值，返回值为被删除的值。key 值必须给出。 否则，返回 default 值。
# pop()方法语法：
# pop(key[,default])
# key: 要删除的键值
# default: 如果没有 key，返回 default 值
# 返回被删除的值。

site = {'name': 'python', 'alexa': 10000, 'url': 'www.baidu.com'}
pop_obj = site.pop('name')
print(pop_obj)
print(site)

# Python 字典(Dictionary) update() 函数把字典dict2的键/值对更新到dict里。
# update()方法语法：
# dict.update(dict2)
# dict2 -- 添加到指定字典dict里的字典。
dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }

dict.update(dict2)
print dict

# Python 字典(Dictionary) clear() 函数用于删除字典内所有元素。
# clear()方法语法：
# dict.clear()

dict = {'Name': 'Zara', 'Age': 7};
print "Start Len : %d" %  len(dict)
dict.clear()
print "End Len : %d" %  len(dict)

# Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
# fromkeys()方法语法：
# dict.fromkeys(seq[, value])
# seq -- 字典键值列表，可以是字符串、数组、元组
# value -- 可选参数, 设置键序列（seq）的值。

seq = 'Google'
seq = ('Google', 'Runoob', 'Taobao')
seq = ['Google', 'Runoob', 'Taobao']
 
dict = dict.fromkeys(seq)
print "新字典为 : %s" %  str(dict)
 
dict = dict.fromkeys(seq, 10)
print "新字典为 : %s" %  str(dict)