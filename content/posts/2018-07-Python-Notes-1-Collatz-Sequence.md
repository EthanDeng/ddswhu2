---
title: Python Notes 1 - Collatz Sequence
date: '2018-07-04'
slug: python note collatz sequence
draft: false
author: Dongsheng Deng @
categories:
  - Python
tags:
  - Python
  - collatz
  - recursive
---


## 1. 定义函数实现循环调用

### 1.1 问题描述 --- Collatz 序列

编写一个名为 `collatz()` 的函数，它有一个名为 `number` 的参数。如果参数是偶数，那么 `collatz()` 返回 `number//2`，并返回该值。如果 `number` 为奇数，`collatz()` 打印并返回 `3*number+1`。

然后编写一个程序，让用户输入一个整数，并不断对这个数调用 `collatz()`，直到函数返回值为 1。

> 1. 记得将 input() 的返回值用 int() 函数转为一个整数，否则它会是一个字符串。
> 2. number %2 == 0，整数 number 就是偶数，如果 number %2 == 1，它就是奇数。

这个程序的输出结果应该像如下： 

```python
Enter number:
3
10
5
16
8
4
2
1
```


### 1.2 解决方法

思路：利用 while 进行判断，让 collatz 自己循环调用自己。([代码下载](/posts/archive/collatz.py))

```python
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3*number + 1)
        return 3*number + 1

n = input("Enter number: \n")

while n != 1:
    n = collatz(number=int(n))
```

## 2. 输入验证

在前面的项目中添加 `try` 和 `except` 语句，检测用户是否输入了一个非整数的字符串。

> 正常情况下， int() 函数传入了一个非整数字符串时，会产生 ValueError 错误。

### 2.1 解决方法 
思路：在外层套一个 `try except` 即可。([代码下载](/posts/archive/input_verify.py))

```python
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3*number + 1)
        return 3*number + 1

n = input("Enter number: \n")


try:
    number = int(n)
    while number != 1:
        number = collatz(number=number)
except:
    print("Please input an integer!")
```

## Reference

+ [Making a collatz program automate the boring stuff](https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff)

