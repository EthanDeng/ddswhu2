---
title: Basic Configuration of Cmder
date: '2018-07-05'
slug: configuration of Cmder
draft: false
author: Dongsheng Deng @
categories:
  - Tools
tags:
  - Tools
  - Cmder
---

## 1. 让 Cmder 显示中文

打开 Cmder 设置选项，找到 `Startup-Environment`，在右边添加下面代码

```shell
set LANG=zh_CN.UTF-8
```

## 2. 修改 Cmder 默认打开目录

打开 Cmder 设置选项，找到 `Startup-Tasks`，将右边的 `cmd::Cmder as Admin` 任务运行内容修改为

```shell
*-new_console:d:C:\Users\Ethan cmd /k ""%ConEmuDir%\..\init.bat" " 
```
其中将 `C:\Users\Ethan` 替换为自己想要的启动目录。

然后类似的将 `cmd::Cmder` 任务的运行内容替换为 

```shell
-new_console:d:C:\Users\Ethan cmd /k ""%ConEmuDir%\..\init.bat" "
```

## 3. 修改命令提示符

Cmder 默认的命令提示符是 `λ`，如果想改成常见的 `$`，只需要找到 Cmder 的安装目录下的 vendor 目录（我的是 `C:\Program Files\cmder\vendor`），然后将 `clink.lua` 文件中 `λ` 修改为 `$` 即可。具体的，可以在 `clink.lua` 文件中搜索 `λ`（大约在第 43 行）。修改之后 43 行代码为

```lua
    local lambda = "$"
```

## 4. 添加 Cmder 到右键菜单选项

以管理员权限运行 Cmder，然后运行下面代码

```shell
Cmder.exe /REGISTER ALL
```
**注意**：前提条件是 Cmder.exe 所在目录已经在系统环境变量（`Path`）中。

## Reference

+ [Cmder 初次使用前的一些常用配置](https://blog.csdn.net/DpangD/article/details/79254951)
