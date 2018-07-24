---
title: Create and Using OCG in LaTeX
date: '2018-07-24'
slug: create ocg in latex
draft: false
author: Dongsheng Deng @
categories:
  - LaTeX
tags:
  - ocgx2
  - ocg
---

## 1. 最初的设想

在学习 Python 的时候，看到一个习题集，每个习题的后面是答案，而网址在每个习题的下面提供了一个点击的按钮，当点击的时候可以显示答案，当时我就想，LaTeX 的宏包有没有能够实现这个功能的？顺藤摸瓜找到了 ocg 包，然后其进化版 ocgx，以及最终进化版 ocgx2。

OCG（Optional Content Groups），暂译为可选内容组，指的是在 PDF 中嵌套可选可视的内容。比如加入图层（layer），在查看的时候，通过不同的图层搭配可以显示不同的效果。

## 2. ocgx2 包介绍

[ocgx2](https://gitlab.com/agrahn/ocgx2) 是 Alexander Grahn 从 2015 年开始开发并维护至今的一个用于创建 PDF 图层，管理 ocg 的包，它的作用是想完全替换掉目前 Paul Gaborit 的 ocgx 包和 Werner Moshammer 的 ocg-p 包，因为后两者都有自己的局限性。相比初代 ocg，ocgx 和 ocg-p 包，ocgx2 完全实现了这几个包的功能，并且解决了编译引擎上的局限，现在 ocgx2 支持

+ LaTeX ⇒ dvips ⇒ ps2pdf/Distiller
+ (Xe)LaTeX ⇒ (x)dvipdfmx
+ pdfLaTeX, LuaLaTeX

并且 ocgx2 改善了在处理 PDF 图层时的性能，也提高与其他包同时加载时的兼容性。更为重要的，ocgx2 新增加图层跨页功能，之前宏包没法跨页。

## 3. ocgx2 宏包设定
### 3.1 为 ocg 对象链接添加颜色

```tex
\usepackage{hyperref}  % do NOT set [ocgcolorlinks] here!
\usepackage[ocgcolorlinks]{ocgx2}
```

### 3.2 为 TikZ 提供图层支持

```tex
\usepackage[tikz]{ocgx2}
```

## 4. ocgx2 宏包使用

### 4.1 ocg 定义方法
我们是通过 ocg 环境定义一个 ocg 图层的，语法如下

```tex
\begin{ocg}[<options>]{<layer name>}{<layer id>}{<initial visibility>}
  ... material to be put on a PDF layer ...
\end{ocg}
```
其中 `options` 一般不填，想了解的可以看下 ocgx2 官网对这部分的解释。`layer name` 是第一个必选项，意为当前创建的 ocg 的图层名字，在之后并不会调用，在阅读 PDF 的时候能够用于分辨不同图层。`layer id` 是为当前 ocg 创建的 ocg 的 id（唯一识别）。不同的 ocg 的 id 都应该不一样。`initial visibility` 指的是为当前 ocg 指定默认的可见性。1 为可见（visible），0 为不可见（invisible）。

### 4.2 ocg 图层间切换
ocgx2 提供了 4 个核心命令用于切换 ocg 图层

```tex
\switchocg{待切换的图层 id，逗号分隔}{<link text>}
\showocg{待显示的图层 id，逗号分隔}{<link text>}
\hideocg{待隐藏的图层 id，逗号分隔}{<link text>}
\actionsocg{待切换的图层（X）}{待显示的图层（Y）}{待隐藏的图层（Z）}{<link text>}
```
其中 `link text` 是一段文字，在 PDF 的效果是，当鼠标点击 `link text` 的时候，图层会进行切换，显示或者隐藏。图层 id 可以为多个，并用英文分号隔开即可。需要注意的是 `\actionsocg` 是为 `link text` 指定一系列动作，即在点击 `link text` 的时候，**同时** X 的所有图层状态切换（`可见` <-> `不可见`），Y 所有图层全部变为 `可见`，Z 所有图层全部变为 `不可见`。

一个简单的示例如下：

```tex
\switchocg{ocg1}{\textbf{Show answer}}

\begin{ocg}{Python Code}{ocg1}{1}
\begin{verbatim}
import requests
url = 'www.example.com'
reponse = request.get(url=url).content
print(response)
\end{verbatim}
\end{ocg}
```
在点击 `Show answer` 之后，下面的这段代码就能切换显示状态。

### 4.3 与 TikZ 结合使用
为了让 ocg 与 TikZ 结合非常简单，只需要在 TikZ 环境中，用 ocg 环境包裹 TikZ 绘图命令即可。比如

```tex
\begin{tikzpicture}[node distance=3cm, state/.style={fill=green!20},auto]

\begin{ocg}{grid}{ocgridid}{1}
\draw[black!20] (-1,-1) grid (4,2);
\end{ocg}

\begin{ocg}{states}{ocstatesid}{1}
\node[state] (q_a) {$q_a$};
\node[state] (q_b) [right of=q_a] {$q_b$};
\end{ocg}

\begin{ocg}{edges}{ocedgesid}{1}
\path[->]
(q_a) edge node {0} (q_b)
edge [loop above] node {0} ()
(q_b) edge [loop above] node {1} ();
\end{ocg}

\end{tikzpicture}
```

最后，这里给出一个效果图（[源码下载](/posts/archive/ocg.tex)，[PDF 下载](/posts/archive/ocg.pdf)）：

<center><img src='/posts/image/ocg.gif' width=480px/></center>


## Reference

+ [ocgx2: LaTeX package for creating PDF Layers (OCG)](https://gitlab.com/agrahn/ocgx2)
+ [Using TikZ and ocgx2](https://www.overleaf.com/18083402qmjzhzbdkmww#/68448141/)
