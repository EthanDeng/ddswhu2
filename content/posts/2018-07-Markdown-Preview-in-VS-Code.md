---
title: Markdown Preview in Visual Studio Code
date: '2018-07-11'
slug: markdown preview in vs code
draft: false
author: Dongsheng Deng @
categories:
  - Tools
tags:
  - VS Code
  - Markdown
---

## 介绍

> Markdown Preview Enhanced 是一款为 Atom 以及 Visual Studio Code 编辑器编写的超级强大的 Markdown 插件。 这款插件意在让你拥有飘逸的 Markdown 写作体验。

我们先来看下官网的效果：

<center>![效果图](/posts/image/mdpreenhance.png)</center>

## 安装
Markdown Preview Enhanced 的安装非常简单，打开 VS Code 之后，在插件管理，搜索 Markdown Preview Enhanced 这个插件，并选择安装，安装好之后重新加载就行了。

## 预览配置

我们编写 Markdown 之后，在 VS Code 右上角有一个预览的按钮，点击预览按钮之后，会弹出 Markdown 的预览界面。不过预览界面在 Windows 上的效果并不太好（主要是字体问题）。而我选择 MPE 的原因就在于它支持你自己定义预览显示，并且也支持输出 Html 或者 PDF 格式。

根据 MPE 的[文档说明](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/)，在[自定义 CSS 部分](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/customize-css)，我们可以根据文档对我们的预览进行修改。下面是我自己的预览设置。

```css
.markdown-preview.markdown-preview {

    font-size: 17px;

    font-family: "Myriad Pro","文泉驿微米黑";

    pre, code {
        font-family: 'Menlo';
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Myriad Pro','黑体';
    }

    h1{
        font-size: 28px;
    }
    h2{
        font-size: 25px;
    }
    h3{
        font-size: 22px;
    }
    h4, h5 {
        font-size: 20px;
    }
}
```
修改好预览设置之后，我们可以看下显示的效果：

<center>![效果图](/posts/image/mpe.png)</center>

## Reference

+ [自定义 CSS](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/customize-css)


