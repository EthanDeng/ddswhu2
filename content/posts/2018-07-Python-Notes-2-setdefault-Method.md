---
title: Python Notes 2 - setdefault Method
date: '2018-07-05'
slug: python note setdefault method
draft: false
author: Dongsheng Deng @
categories:
  - Python
tags:
  - Python
  - dict
  - setdefault
---


## 1. 字典中 setdefault 方法怎么理解？

### 1.1 问题描述

参考菜鸟教程中 setdefault 的描述：[Python3 字典 setdefault() 方法](http://www.runoob.com/python3/python3-att-dictionary-setdefault.html)

> Python 字典 setdefault() 方法和 get() 方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。

字典的 setdefault 方法与字典赋值有什么区别？

### 1.2 语法区别

setdefault() 方法的语法：

```python
dict.setdefault(key, default=None)
```

直接赋值方法：

```python
dict['key'] =  value
```

### 1.3 理解 setdefault 方法

```python
# 字典的 setdefault 方法的用途是给一个字典某个 key 指定默认的 value
# 在 key 不存在的时候，会新建 key-value 对
# 但是当 key 存在的时候，setdefault 不会更改这个 key 所对应的 value。

spam = {'Name': 'Runoob', 'Age': 7}

spam.setdefault('Age','25')
spam.setdefault('Sex', 'NA')
spam.setdefault('School')

print ("Age 键的值为 : %s" % spam['Age']) #  Age 键存在在字典中，则不会设置 Age=25
print ("Sex 键的值为 : %s" % spam['Sex']) # Sex 键不存在，所以 Sex 会被指定为 NA
print ("School 键的值为 : %s" % spam['School']) # School 键不存在，不指定值，默认为 None
spam['Sex']="Female"
print ("新字典为：", spam)
```
运行 [代码](/posts/archive/setdefault.py) 之后，所得到的打印结果为

```shell
Age 键的值为 : 7
Sex 键的值为 : NA
School 键的值为 : None
新字典为： {'Name': 'Runoob', 'Age': 7, 'Sex': 'Female', 'School': None}
[Finished in 0.5s]
```

### 1.4 setdefault 方法与 直接赋值示例

```python
# 本函数用来计算 msg 中每个字母出现的次数.
msg = "Economics"

count = {}
n = 1

for character in msg:
    # 对于 count 这个 dict，因为之前声明为空 dict，所以对于任何 key 都没有指定 value
    # 所以在每次遇到【新】字母的时候 setdefault 会把每个 character 作为 key，并且指定 value 为 0
    # 因为字母 o 在第三次循环的是已经更新过了，所以在第五次的时候，字母 o 这个 key 的 setdefault 语句是无效的。
    count.setdefault(character,0) 

    # 这个语句只是普通的字典更新的方法，dict[key] = value：将 key 的值设定为 value
    count[character] = count[character] + 1
    
    print("第",n,"次循环的时，count 的值",count)

    # 记录循环次数
    n += 1
```
运行 [代码](/posts/archive/dict_asign_diff.py) 之后，所得到的打印结果为

```python
第 1 次循环的时，count 的值 {'E': 1}
第 2 次循环的时，count 的值 {'E': 1, 'c': 1}
第 3 次循环的时，count 的值 {'E': 1, 'c': 1, 'o': 1}
第 4 次循环的时，count 的值 {'E': 1, 'c': 1, 'o': 1, 'n': 1}
第 5 次循环的时，count 的值 {'E': 1, 'c': 1, 'o': 2, 'n': 1}
第 6 次循环的时，count 的值 {'E': 1, 'c': 1, 'o': 2, 'n': 1, 'm': 1}
第 7 次循环的时，count 的值 {'E': 1, 'c': 1, 'o': 2, 'n': 1, 'm': 1, 'i': 1}
第 8 次循环的时，count 的值 {'E': 1, 'c': 2, 'o': 2, 'n': 1, 'm': 1, 'i': 1}
第 9 次循环的时，count 的值 {'E': 1, 'c': 2, 'o': 2, 'n': 1, 'm': 1, 'i': 1, 's': 1}
```

## Reference

+ [Python3 字典 setdefault() 方法](http://www.runoob.com/python3/python3-att-dictionary-setdefault.html)
