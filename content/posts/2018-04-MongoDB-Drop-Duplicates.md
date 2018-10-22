---
title: Remove Duplicates in MongoDB
date: '2018-04-27'
slug: drop duplicates in mongodb
draft: false
author: Dongsheng Deng @
categories:
  - MongoDB
tags:
  - MongoDB
---

如果我们想根据一个变量，比如 `loan_id` 来删除 my_collection 中重复的 document，可以使用下面的命令

```shell
db.my_collection.aggregate([
    {
        $group: { _id: {loan_id: '$loan_id'},count: {$sum: 1},dups: {$addToSet: '$_id'}}
    },
    {
        $match: {count: {$gt: 1}}
    }
],{ allowDiskUse: true }).forEach(function(doc){
    doc.dups.shift();
    db.my_collection.remove({_id: {$in: doc.dups}});
})
```

这段代码的含义就是根据 `loan_id` 进行分类汇总，然后计数，如果多于 1，则将其删除。


[How to remove duplicates in mongodb][remove]
[Fastest way to remove duplicate documents in mongodb][remove2]

[remove]: https://weknowinc.com/blog/how-remove-duplicates-in-mongodb
[remove2]: https://stackoverflow.com/questions/14184099/fastest-way-to-remove-duplicate-documents-in-mongodb
