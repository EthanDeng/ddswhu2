---
title: Configure Sublime Text 3 as LaTeX IDE
date: '2018-06-03'
author: Dongsheng Deng @
slug: sublime text for latex
draft: false
categories:
  - LaTeX
tags:
  - LaTeX
  - Editor
  - Sublime Text 3
---

> 本教程配有视频，视频下载链接：[下载地址](https://mp.weixin.qq.com/s/3FXTI3t-L_0OBWtoxfmOgQ)

Sublime Text 是一个轻量级的、跨平台的编辑器，搭配 LaTeXTools 和 TeX Live 或者 MiKTeX 使用可以编译 TeX 文件。以前你可能会觉得 LaTeX 命令很难记得住，写起来很麻烦，但是借助 Sublime Text 里面的 LaTeXTools 插件你会觉得写 TeX 文档也可以是一种享受。从我自身的经验来看，自从配置好 Sublime Text 之后，我再没回去用 TeXworks 或者 WinEdt。

在 2014 年，我在自己博客上发布了如何使用 Sublime Text 搭建 LaTeX 编写环境，这么多年了，我的主页 发生了更迭，那篇帖子早已不见了，不过网上倒是能找到一些转载的内容。当时我将那篇帖子投稿到 LaTeX Studio，有兴趣的可以看下，传送门：[Sublime Text 搭建 LaTeX 编写环境](http://www.latexstudio.net/archives/1169)。时间过了这么多年，LaTeXTools 插件也发生了一些改变，原来的帖子感觉有点不合时代了，所以决定更新下。

**Sublime Text 3 的界面图**

<center>![效果图](/posts/image/sublime.png)</center>

## 2. 准备工作
首先，为了搭建 LaTeX 工作环境，你需要安装：

+ TeX Live 或者 MiKTeX （本文以 TeX Live 2017 为例）
+ Sublime Text 3
+ Package Control (Sublime Text 插件)
+ LaTeXTools （Sublime Text 插件）
+ SumatraPDF 阅读器（可选，用于预览 PDF）

在上述软件/插件安装之后，你需要把 TeX Live 的 bin 目录（`D:\Program Files\texlive\2017\bin\win32`）以及 SumatraPDF 的路径（`C:\Program Files (x86)\SumatraPDF`）添加到系统环境变量（`PATH`）中。

### 2.1 安装插件
#### 2.1.1 安装 Package Control
打开 Sublime Text 的包管理工具 Package Control 的[安装介绍界面](https://packagecontrol.io/installation)，选择 Sublime Text 3 版本的安装命令（如下）并复制

```python
import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```
然后，打开 Sublime Text，按住快捷 ` Ctrl+~`（或者 `View -> Show Console`）打开控制台，然后将上述代码粘贴到 Console 里面，完成 Package Control 的安装。

#### 2.1.2 安装 LaTeXTools
在 Sublime Text 内，按住 `Ctrl+Shift+P` 打开命令选项板（Command Palette），选择 `Package Control: Install Package`，然后找到 `LaTeXTools`，选择安装即可。

### 2.2 添加环境变量
Win10 中将路径添加到环境变量中的步骤如下：右键我的电脑，然后选择 `属性`，在左侧选择 `高级系统设置`，然后选择下方的 `环境变量`，选择变量 `Path` 编辑，将需要添加的路径添加进去即可。

## 3. 配置过程
### 3.1 配置 LaTeXTools
改版之后的 LaTeXTools 配置起来非常方便，只需要修改用户设置文件，依次选择 `Preferences -> Package Settings -> LaTeXTools -> Settings – User`，打开 LaTeXTools.sublime-settings 这个文件，根据自己的操作系统修改 TeX 的路径（在 200 行左右），选择对应的发行版本，然后修改用于预览的 PDF 阅读器的路径（推荐 SumatraPDF，如果已经添加到系统路径，则 `sumatra` 不需要设置），以及指定 Sublime Text 的路径，修改之后的 LaTeXTools.sublime-settings 文件如下所示

```json
  "windows": {
    "texpath" : "D:\\Program Files\\texlive\\2017\\bin\\win32",
    "distro" : "texlive",
    "sumatra": "",
    "sublime_executable": "",
    "keep_focus_delay": 1200
  },
```

### 3.2 反向搜索设置
由于 SumatraPDF 反向搜索的选项配置是隐藏的，因此，我们这里先编译一个 LaTeX 的例子，将下面的代码复制到 Sublime Text 里面

```tex
%!TEX program = pdflatex

\documentclass{article}

\title{test}
\author{ddswhu}
\date{\today}
 
\begin{document}
\maketitle
 
This is the context of the article.
 
\end{document}
```
保存为 `test.tex`，再按组合键 `Ctrl+B` 编译，SumatraPDF 就会自动弹出，显示 `test.pdf` 的内容，然后在 SumatraPDF 上方的菜单栏选择 `设置`，将下面的代码添加到 SumatraPDF 选项的最下面方的反向搜索设置框内即可。

```shell
"C:\Program Files\Sublime Text 3\sublime_text.exe" "%f:%l"
```

确定然后关闭。这样，我们就设置好了 SumatraPDF 的反向搜索。至此，我们已经搭建好了 Sublime Text 用于编辑 LaTeX 的环境。

## Reference

+ [https://packagecontrol.io/installation](https://packagecontrol.io/installation)
+ [https://latextools.readthedocs.io/en/latest/install/](https://latextools.readthedocs.io/en/latest/install/)
+ [Sublime Text 搭建 LaTeX 编写环境](http://www.latexstudio.net/archives/1169)
