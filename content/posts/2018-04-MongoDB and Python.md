---
title: Start MongoDB as service
date: '2018-04-13'
slug: start mongodb as service
draft: false
author: Dongsheng Deng @
categories:
  - Python
tags:
  - Python
  - MongoDB
---

## 1. start MongoDB normally

Once you have installed MongoDB on your PC, you can start MongoDB using 

```shell
mongod --dbpath C:\MongoDB\Server\3.6\data\db
```

## 2. start MongDB as service

1. remove the existing MongDB service
2. intall the MongoDB as a service
3. start the MongoDB service
4. stop the MongoDB service

```shell
mongod --remove 
mongod --dbpath=C:\MongoDB\Server\3.6\data\db --logpath=C:\MongoDB\Server\3.6\logs\log.txt --install
net start MongoDB
net stop MongoDB
```

When you install or remove MongoDB *service* to or from you computer, you can add the `--serviceName YourServiceName` flag after the command to customize the
service name as you wish.  

> If needed, you can install services for multiple instances of mongod.exe. Install each service with a unique --serviceName and --serviceDisplayName. Use multiple instances only when sufficient system resources exist and your system design requires it.

## Reference 

+ [Manual of mongod.exe](https://docs.mongodb.com/manual/reference/program/mongod.exe/)
+ [How to run MongoDB as Windows service?
](https://stackoverflow.com/questions/2438055/how-to-run-mongodb-as-windows-service)
