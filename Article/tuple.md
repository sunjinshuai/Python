# Tuple #

Python 的元组与列表类似，不同之处在于元组的元素不能修改。
* 元组使用小括号，列表使用方括号。
* 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

```
tup1 = ('Pyton', 'iOS');
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";   #  不需要括号也可以
```

## 创建 tuple ##

创建空元组

```
tuple = ()
```

元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：

```
tup1 = (50)
type(tup1) 

<class 'int'> # 不加逗号，类型为整型

tup1 = (50,)
type(tup1)

<class 'tuple'> # 加上逗号，类型为元组
```

## 访问元组 ##

元组可以使用下标索引来访问元组中的值，如下实例:

```
tup1 = ('Pyton', 'iOS');
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";   #  不需要括号也可以

print ("tup1[0]: ", tup1[0])
print ("tup2[1:3]: ", tup2[1:3])

tup1[0]:  Pyton
tup2[1:5]:  (2, 3, 4)
```

## 修改元组 ##

元组中的元素值是不允许修改的，但可以对元组进行连接组合，如下实例:

```
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2;
print (tup3)

(12, 34.56, 'abc', 'xyz')
```

## 删除元组 ##

元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:

```
tup = ('Pyton', 'iOS', 'Java', 'C');
 
print (tup)
del tup;
print ("删除后的元组 tup : ")
print (tup)
```

如果元组被删除后，再次访问会有异常信息

```
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    print (tup)
NameError: name 'tup' is not defined
```

## 元组索引、截取

```
L = ('Python', 'iOS', 'Jav')

print L[2]  # 读取第三个元素
print L[-2] # 从右侧开始读取倒数第二个元素: count from the right
print L[1:] # 输出从第二个元素开始后的所有元素
```

## tuple 运算符 ##

与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

|Python 表达式|结果|描述|
|-----------|-----|-----|
|len((1, 2, 3))|3|计算元素个数|
|(1, 2, 3) + (4, 5, 6)|(1, 2, 3, 4, 5, 6)|连接|
|('Hi!',) * 4|('Hi!', 'Hi!', 'Hi!', 'Hi!')|复制|
|3 in (1, 2, 3)|True|元素是否存在|
|for x in (1, 2, 3): print x,|1 2 3|迭代|

## 7、元组内置函数 ##

|方法|描述|
|----|----|
|cmp(tuple1, tuple2)|比较两个元组元素|
|len(tuple)|计算元组元素个数|
|max(tuple)|返回元组中元素最大值|
|min(tuple)|返回元组中元素最小值|
|tuple(seq)|将列表转换为元组|
