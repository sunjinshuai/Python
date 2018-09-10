## 编码

`Python` 中默认的编码格式是 `ASCII` 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
解决方法为只要在文件开头加入 `# -*- coding: UTF-8 -*-` 或者 `#coding=utf-8` 就行了
**注意：`#coding=utf-8` 的 `=` 号两边不要空格。**

## Python 标识符

* 标识符由字母、数字、下划线组成。
* 所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。

`Python` 中的标识符是区分大小写的，以下划线开头的标识符是有特殊意义的：
* 以单下划线开头 `_foo` 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 `from xxx import *` 而导入；
* 以双下划线开头的 `__foo` 代表类的私有成员；以双下划线开头和结尾的 `__foo__` 代表 `Python` 里特殊方法专用的标识，如 `__init__()` 代表类的构造函数。

`Python` 可以同一行显示多条语句，方法是用分号 `;` 分开，如：

```
print 'hello';print 'world';
hello
world
```

## Python 保留字符

下面的列表显示了在 `Python` 中的保留字。这些保留字不能用作常数或变数，或任何其他标识符名称，所有 `Python` 的关键字只包含小写字母，比如：

```
and	exec	not
assert	finally	or
break	for	pass
class	from	print
continue	global	raise
def
```

## 行和缩进

`Python` 的代码块不使用大括号 `{}` 来控制类，函数以及其他逻辑判断，`Python` 最具特色的就是用缩进来写模块，如果不严格使用缩进，会报如下错误。
```
IndentationError: unindent does not match any outer indentation level错误表明，你使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可。
```

**每个缩进层次使用单个制表符、两个空格或四个空格，切记不能混用。**

## Python 引号

`Python` 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。

```
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
```

## Python注释

`Python` 中单行注释采用 # 开头。

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

# 第一个注释
print "Hello, Python!";  # 第二个注释
```

`Python` 中多行注释使用三个单引号(''')或三个双引号(""")。

```
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
```

## Python 空行

函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是 `Python` 语法的一部分。书写时不插入空行，`Python` 解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

**记住：空行也是程序代码的一部分。**

* 模块级函数和类定义之间空两行；
* 类成员函数之间空一行；

```python
class A:

    def __init__(self):
        pass

    def hello(self):
        pass


def main():
    pass   
```

* 可以使用多个空行分隔多组相关的函数
* 函数中可以使用空行分隔出逻辑相关的代码

## 空格

* 在二元运算符两边各空一格`[=,-,+=,==,>,in,is not, and]`:

```python
# 正确的写法
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# 不推荐的写法
i=i+1
submitted +=1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

* 函数的参数列表中，`,`之后要有空格

```python
# 正确的写法
def complex(real, imag):
    pass

# 不推荐的写法
def complex(real,imag):
    pass
```

* 函数的参数列表中，默认值等号两边不要添加空格

```python
# 正确的写法
def complex(real, imag=0.0):
    pass

# 不推荐的写法
def complex(real, imag = 0.0):
    pass
```

* 左括号之后，右括号之前不要加多余的空格

```python
# 正确的写法
spam(ham[1], {eggs: 2})

# 不推荐的写法
spam( ham[1], { eggs : 2 } )
```

* 字典对象的左括号之前不要多余的空格

```python
# 正确的写法
dict['key'] = list[index]

# 不推荐的写法
dict ['key'] = list [index]
```

* 不要为对齐赋值语句而使用的额外空格

```python
# 正确的写法
x = 1
y = 2
long_variable = 3

# 不推荐的写法
x             = 1
y             = 2
long_variable = 3
```

## 换行

`Python` 语句中一般以新的换行符作为语句的结束符，但是我们可以使用斜杠`（ \）`将一行的语句分为多行显示，如下所示：

```
total = item_one + \
        item_two + \
        item_three
```

元祖、列表和字典除外，

```
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
```

Python 支持括号内的换行。这时有两种情况。

1) 第二行缩进到括号的起始处

```python
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```

2) 第二行缩进 4 个空格，适用于起始括号就换行的情形

```python
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```

使用反斜杠`\`换行，二元运算符`+` `.`等应出现在行末；长字符串也可以用此法换行

```python
session.query(MyTable).\
        filter_by(id=1).\
        one()

print 'Hello, '\
      '%s %s!' %\
      ('Harry', 'Potter')
```

禁止复合语句，即一行中包含多个语句：

```python
# 正确的写法
do_first()
do_second()
do_third()

# 不推荐的写法
do_first();do_second();do_third();
```

`if/for/while`一定要换行：

```python
# 正确的写法
if foo == 'blah':
    do_blah_thing()

# 不推荐的写法
if foo == 'blah': do_blash_thing()
```
