print "Hello, Python!";


# Python 标识符
# 在 Python 里，标识符由字母、数字、下划线组成。
# 在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
# Python 中的标识符是区分大小写的。
# 以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
# 以双下划线开头的 __foo 代表类的私有成员；以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。


# 行和缩进
# Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
# 缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。如下所示

"""
if True:
    print "True"
else:
    print "False"

if True:
    print "Answer"
    print "True"
else:
    print "Answer"
    # 没有严格缩进，在执行时会报错
  print "False"

注意：
File "/Users/sunjinshuai/Desktop/Python/basic_grammar.py", line 27
    print "False"
        ^  
IndentationError: unindent does not match any outer indentation level
错误表明，你使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可。
"""

# Python注释
# python中单行注释采用 # 开头。
print "Hello, Python!";  # 第一个注释
# python 中多行注释使用三个单引号(''')或三个双引号(""")。

# Python 引号

# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。

word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

print word
print sentence
print paragraph