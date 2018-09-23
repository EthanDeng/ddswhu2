---
title: Get the Summary Statistics and Wirte it to CSV/Excel
date: '2018-09-23'
author: Dongsheng Deng @
slug: summary statistics and write csv
draft: false
categories:
  - Python
tags:
  - Function
  - Describe
  - Summary Statistics
---

## 1. 问题描述
在使用 Python 进行数据分析的时候，在对数据清洗完毕之后，一般我们需要对数据进行描述统计，怎么利用 Python 对数据进行基础描述统计呢？更复杂的，如何获得更多的统计量的信息？最后怎么把描述统计的表导出到本地 csv/excel 文件？

## 2. 问题初探

Pandas 包自带了一个函数 describe，它能直接获得数据的基础描述统计，例如 
```python
import pandas as pd
tlr2agonist = pd.DataFrame({'Mol_Weight':      [4, 5, 7], 
                            'AsymmetricAtoms': [1, 2, 8],
                            'ChiralAtoms':     [3, 8, 9]
                  })
tlr2agonist.describe()
```
它的输出为

```python
         Mol_Weight  AsymmetricAtoms      ChiralAtoms
count      3.000000         3.000000         3.000000
mean       5.333333         3.666667         6.666667
std        1.527525         3.785939         3.214550
min        4.000000         1.000000         3.000000
25%        4.500000         1.500000         5.500000
50%        5.000000         2.000000         8.000000
75%        6.000000         5.000000         8.500000
max        7.000000         8.000000         9.000000
```

describe 结果看起来不错，但是当我们想要峰度（kurtosis）和偏度（skewness） 的时候，好像 describe 函数并不方便。其实 pandas 里面自带峰度偏度的计算公式，

```python
>>> s = pd.Series(range(100))
>>> print("序列 s 的峰度是", s.kurt())
>>> print("序列 s 的偏度是", s.skew())
序列 s 的峰度是 -1.2
序列 s 的偏度是 0.0
```

但是，这个怎么放入到 describe 生成的描述统计表中呢？

## 3. 解决方法
一开始我们想直接以 pandas 行的形式添加进去，可以实现，但是它的 row index 会消失，这个时候需要重新 set index，参考了 Stack Overflow 上的回答，我们给出下面自定义函数

```python
def describe(df, stats):
    d = df.describe()
    return d.append(df.reindex(d.columns, axis="columns").agg(stats))
```

其中第一个参数传入的是需要进行描述统计的 data frame，而第二个参数是指相较于 describe 需要补充的统计量的列表，比如峰度（kurt），偏度（skew）等，更多统计量信息参考 [pandas](http://pandas.pydata.org/pandas-docs/stable/api.html#id39)。示例

```python
describe(tlr2agonist, ['kurt', 'skew'])
```
此时输出结果为 
```python
       Mol_Weight  AsymmetricAtoms    ChiralAtoms
----------------------------------------------------
count    3.000000         3.000000       3.000000
mean     5.333333         3.666667       6.666667
std      1.527525         3.785939       3.214550
min      4.000000         1.000000       3.000000
25%      4.500000         1.500000       5.500000
50%      5.000000         2.000000       8.000000
75%      6.000000         5.000000       8.500000
max      7.000000         8.000000       9.000000
----------------------------------------------------
kurt        NaN             NaN             NaN
skew     0.935220         1.597097      -1.545393
```

## 4. 扩展

如果我们有多个子数据集（subsample data），我们需要对他们分别进行描述统计，并且追加到上面的表格中，应该怎么做？

为了区分数据集，这个时候，我们需要在描述统计的表格添加一列 dataset，用以填写数据集信息，完整代码如下

```python
import pandas as pd

tlr2agonist = pd.DataFrame({'Mol_Weight':      [4, 5, 7], 
                            'AsymmetricAtoms': [1, 2, 8],
                            'ChiralAtoms':     [3, 8, 9]
                  })

tlr2antagonist = pd.DataFrame({'Mol_Weight':      [8, 5, 9], 
                               'AsymmetricAtoms': [1, 2, 3],
                               'ChiralAtoms':     [7, 8, 9]
                  })


def describe(df, stats):
    d = df.describe()
    return d.append(df.reindex(d.columns, axis="columns").agg(stats))

datasets = ['tlr2agonist','tlr2antagonist']

final_df = pd.DataFrame()

for dataset_s in datasets: // 对子数据集进行循环
    dataset = eval(dataset_s) // 将字符串转为变量名
    sum_stats = describe(dataset, ['skew', 'kurt']) // 计算每个子数据集的描述统计
    sum_stats['dataset'] = dataset_s // 在新的列补充数据集信息
    final_df = final_df.append(sum_stats) // 将不同数据集的描述统计表追加在一起
```
最终的输出结果为

```python
       Mol_Weight  AsymmetricAtoms  ChiralAtoms         dataset
count    3.000000         3.000000     3.000000     tlr2agonist
mean     5.333333         3.666667     6.666667     tlr2agonist
std      1.527525         3.785939     3.214550     tlr2agonist
min      4.000000         1.000000     3.000000     tlr2agonist
25%      4.500000         1.500000     5.500000     tlr2agonist
50%      5.000000         2.000000     8.000000     tlr2agonist
75%      6.000000         5.000000     8.500000     tlr2agonist
max      7.000000         8.000000     9.000000     tlr2agonist
skew     0.935220         1.597097    -1.545393     tlr2agonist
kurt          NaN              NaN          NaN     tlr2agonist
---------------------------------------------------------------
count    3.000000         3.000000     3.000000  tlr2antagonist
mean     7.333333         2.000000     8.000000  tlr2antagonist
std      2.081666         1.000000     1.000000  tlr2antagonist
min      5.000000         1.000000     7.000000  tlr2antagonist
25%      6.500000         1.500000     7.500000  tlr2antagonist
50%      8.000000         2.000000     8.000000  tlr2antagonist
75%      8.500000         2.500000     8.500000  tlr2antagonist
max      9.000000         3.000000     9.000000  tlr2antagonist
skew    -1.293343         0.000000     0.000000  tlr2antagonist
kurt          NaN              NaN          NaN  tlr2antagonist
```

## 5. 将数据写出到 csv
得到了描述统计之后，我们可以利用 `DataFrame.to_csv` 把结果导出到 csv 中，具体命令如下

```python
final_df.to_csv("Final Summary Statistics Result.csv")
```

## Reference

+ [Pandas Describe by - Additional Parameters](https://stackoverflow.com/questions/38545828/pandas-describe-by-additional-parameters)
+ [pandas.DataFrame.reindex](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reindex.html)
+ [Pandas Computations/Descriptive Stats](http://pandas.pydata.org/pandas-docs/stable/api.html#id39)
