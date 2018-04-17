---
title: Configure Visual Stuido Code as LaTeX IDE
date: '2018-04-17'
author: Dongsheng Deng @
slug: vs code for latex
draft: false
categories:
  - LaTeX
tags:
  - LaTeX
  - Editor
  - Visual Stuido Code
---

本文介绍如何配置 Visual Studio Code 作为 LaTeX 的编辑器。

## 1. 为什么用 Visual Studio Code
Visual Studio Code（以下简称 VS Code） 是微软推出的一个编辑器，它的优点你可以百度一下，这里不赘述。对我来说，它最有吸引力的当属在 Windows 系统，它对于中英文字体的渲染。如果你原来用过其他编辑器，你就知道在普通屏幕上，中英文的显示效果简直是灾难。我原来因为编辑器的中文显示（当然还有 Terminal 的吸引力）一度想买 Mac，当然最后因为对性能和颜值的追求并不匹配我的财力，加上 Windows 上有些软件不能舍弃，最后作罢。

**注**：高分屏加上合适的字体，Sublime Text 的显示效果也非常好。

**Visual Studio Code 的界面图**

<center>![效果图](/posts/image/vs code.png)</center>

## 2. 准备工作
首先，为了搭建 LaTeX 工作环境，你需要安装：

+ TeX Live 或者 MiKTeX （本文以 TeX Live 2017 为例）
+ Visual Studio Code
+ LaTeX Workshop （VS Code 插件）
+ SumatraPDF 阅读器（可选，用于预览 PDF）

在上述软件/插件安装之后，你需要把 TeX Live 的 bin 目录（`D:\Program Files\texlive\2017\bin\win32`）以及 SumtraPDF 的路径（`C:\Program Files (x86)\SumatraPDF`）添加到系统环境变量（`PATH`）中。

### 2.1 安装插件
VS Code 中插件安装方法如下：在左侧点击扩展按钮（KEY：`Ctrl+Shift+X`）,然后搜索插件名字 LaTeX Workshop，选择安装即可。

### 2.2 添加环境变量
Win10 中将路径添加到环境变量中的步骤如下：右键我的电脑，然后选择 `属性`，在左侧选择 `高级系统设置`，然后选择下方的 `环境变量`，选择变量 `Path` 编辑，将需要添加的路径添加进去即可。

## 3. 配置编译方式与编译组合
VS Code 在今年经历了一次大改之后，配置比原来简单了。它们把过去的 `tool.chain` 改为了 `recipe`，其实本质上是一样的。

### 3.1 编译方式（`tool`）
VS Code 默认添加了3个编译工具（tools）：分别是 `latexmk`，`pdflatex` 和 `bibtex`（所有的工具只编译一次）。编译 `tex` 文档方法，使用右键，选择 `Build LaTeX Project`（快捷键：`Ctrl+Alt+B`），默认使用 `latexmk`，查看 PDF 文件使用快捷键：`Ctrl+Alt+V`。

为了添加其他的编译方式（比如 `xelatex`），我们需要修改 LaTeX Workshop 的配置。方法如下：打开 VS Code 的配置（VS Code 界面左下角，点击齿轮按钮，选择设置），在右侧（用户设置）粘贴下面 JSON 片段：

```json
"latex-workshop.latex.tools": [
	    {
	        "name": "xelatex",
	        "command": "xelatex",
	        "args": [
	          "-synctex=1",
	          "-interaction=nonstopmode",
	          "-file-line-error",
	          "%DOC%"
        	]
        },
		  {
	        "name": "pdflatex",
	        "command": "pdflatex",
	        "args": [
	          "-synctex=1",
	          "-interaction=nonstopmode",
	          "-file-line-error",
	          "%DOC%"
	        ]
	      },
      {
      "name": "latexmk",
      "command": "latexmk",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-pdf",
        "%DOC%"
          ]
        },
	    {
	        "name": "bibtex",
	        "command": "bibtex",
	        "args": [
	          "%DOCFILE%"
	    	]
	    }
	],
```

**注意**，虽然左侧插件默认添加了编译方式（`pdflatex` 与 `bibtex`），也必须将其编译方式的设置（比如 `latex` 等）添加到右侧用户设置中。

### 3.2 编译组合（`recipe`）
如果我们要对一个文档/项目完整的编译（比如`pdflatex->bibtex->pdflatex->pdflatex`）我们需要用到编译组合（`recipes`）。LaTeX Workshop 默认添加了两个 `recipes`，分别是 `latexmk` 和 `pdflatex -> bibtex -> pdflatex*2`，可以通过右键文档，选择 `LaTeX Worksho: All Actions`，选择 `Build LaTeX Project`，然后选择适合的编译组合。

我们之前添加了 `xelatex` 编译方式，我们这里配置下 `xelatex` 的完整编译链 `xelatex -> bibtex -> xelatex*2`,另外补充单次编译的 `recipes`。方法和之前类似，打开用户配置文件，将如下 JSON 添加到用户配置中即可。

```json
"latex-workshop.latex.recipes": [
        {
          "name": "PDFLaTeX",
          "tools": [
            "pdflatex"
          ]
      	},
        {
          "name": "XeLaTeX",
          "tools": [
            "xelatex"
          ]
        },
        {
          "name": "latexmk",
          "tools": [
            "latexmk"
          ]
        },
        {
          "name": "BibTeX",
          "tools": [
            "bibtex"
          ]
        },
        {
          "name": "pdflatex -> bibtex -> pdflatex*2",
          "tools": [
            "pdflatex",
            "bibtex",
            "pdflatex",
            "pdflatex"
          ]
        },
        {
          "name": "xelatex -> bibtex -> xelatex*2",
          "tools": [
            "xelatex",
            "bibtex",
            "xelatex",
            "xelatex"
          ]
        }
    ],
```

这里提供一个测试完整编译方式的代码（[tex](/posts/archive/content.tex), [bib](/posts/archive/info.bib), [pdf](/posts/archive/content.pdf)），你可以用来测试能否编译。效果图如下：

<center><img src="/posts/image/example.png" height=500px></center>


### 3.3 指定编译方式
在 Sublime Text 或者 TeX Studio 中，可以在文件的首行指定编译方式（`% !TEX program`）以及主文档（`% !TEX root`），LaTeX Workshop 也把这个功能添加到了其中，使用方法完全一样。`% !TEX program` 和 `% !TEX root` 被称为 Magic Command。

示例如下：

```TeX
% !TEX program = xelatex
\documentclass{article}

\author{Dongsheng Deng}
\title{Configuration of Visual Studio Code for LaTeX Users}

\begin{document}
\maketitle

Example text.

\end{document}
```

将上述代码保存为 `test.tex`，然后使用快捷键 `Ctrl+Alt+B`，系统会自动选择 `xelatex` 作为编译方式。如果没有其他问题，就能正常编译。


## 4 其他配置
## 4.1 配置快捷键
LaTeX Workshop 的快捷键并不友好，我们可以自定义快捷键，方法如下：点击 VS Code 左下角的齿轮（设置），选择 `键盘快捷方式`。

+ 搜索 `latex build`，将默认的快捷方式改为 `Ctrl+B`
+ 搜索 `build with recipe`，将其改为 `Ctrl+R`
+ 搜索 `latex pdf file`，将其改为 `Ctrl+1`
+ 搜索 `close environment`，将其改为 `Ctrl+E`
+ 搜索 `latex compiler log`，将其改为 `Ctrl+L`
+ 你还可以补充其他快捷键。

配置好快捷键之后，之后当你指定了编译方式时可以直接使用快捷键 `Ctrl+B` 编译一次文档。当你需要完整编译整个文档（文献，目录等），使用快捷键 `Ctrl+R`，选择完整的编译方案即可。是不是方便多了？

## 4.2 配置阅读器以及自动编译
还有其他几个设置需要提一下，由于笔记本的屏幕很小，我并不习惯使用 VS Code 自带的 PDF 阅读器作为预览的阅读器，可以设置 `SumatraPDF` 作为 PDF 阅读器。另外，自动编译选项我也选择关闭。

```json
    "latex-workshop.view.pdf.viewer": "external",
    "latex-workshop.latex.autoBuild.onSave.enabled": false,
```

## Reference

+ [Github: LaTeX-Workshop](https://github.com/James-Yu/LaTeX-Workshop)
+ [Visual Studio Code 搭建 LaTeX 编写环境](http://ddswhu.com/visual-studio-code-latex/)
+ [How to turn off matching highlighting](https://stackoverflow.com/questions/39775406/how-to-turn-off-matching-highlighting)
