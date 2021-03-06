# Python 的基本数据类型 #

Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变类型（3 个）：Number（数字）、String（字符串）、Tuple（元组）；</br>
可变类型（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

Python3 在 Python2 的基础上增加了 Set（集合）。

## Number（数字）

Python3 支持 int、float、bool、complex（复数）。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

## String（字符串）

Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

* Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串。
* Python 没有单独的字符类型，一个字符就是长度为1的字符串。
* 字符串可以用+运算符连接在一起，用*运算符重复。
* Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
* Python中的字符串不能改变。

## List（列表）

列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

* List写在方括号之间，元素用逗号隔开。
* 和字符串一样，list可以被索引和切片。
* List可以使用+操作符进行拼接。
* List中的元素是可以改变的。

## Tuple（元组）

元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

* 与字符串一样，元组的元素不能修改。
* 元组也可以被索引和切片，方法一样。
* 注意构造包含0或1个元素的元组的特殊语法规则。
* 元组也可以使用+操作符进行拼接。

## Set（集合）

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
基本功能是进行成员关系测试和删除重复元素。

## Dictionary（字典）

字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。

* 字典是一种映射类型，它的元素是键值对。
* 字典的关键字必须为不可变类型，且不能重复。
* 创建空字典使用 { }。

## 布尔值 ##

布尔值和布尔代数的表示完全一致，一个布尔值只有 `True` 、 `False `两种值，要么是 `True`，要么是 `False`，在 Python 中，可以直接用 True、False 表示布尔值（请注意大小写），也可以通过布尔运算计算出来。

布尔值可以用 `and`、`or` 和 `not` 运算。

`and` 运算是与运算，只有所有都为 True，and 运算结果才是 True。

`or` 运算是或运算，只要其中有一个为 True，or 运算结果就是 True。

`not` 运算是非运算，它是一个单目运算符，把 True 变成 False，False 变成 True。


## 空值 ##

基本上每种编程语言都有自己的特殊值——空值，在 Python 中，用 None 来表示
