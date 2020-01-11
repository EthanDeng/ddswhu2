---
title: MongoDB unwind Operations
date: '2018-04-29'
slug: unwind operation in MongoDB
draft: false
author: Dongsheng Deng @
categories:
  - MongoDB
tags:
  - MongoDB
---

Just as the [MongoDB manual](https://docs.mongodb.com/manual/reference/operator/aggregation/unwind/index.html) pointed out: 

>`unwind` deconstructs an array field from the input documents to output a document for each element. Each output document is the input document with the value of the array field replaced by the element.

Here are two different cases in appliaction. It depends how the data is stored.

## 1. M array fields × N observations case

If we have _K_ variables in each document, and the _M_ variables are stored as array field. The value of each array field is a list of length _N_, corresponding to the _N_ observations of the variable (i.e. array field).

I take the previous example for illustration. The document is

```json
{ 
    "_id" : ObjectId("5ad08bf9d1673e1e60f97725"), 
    "date" : [
        "2017-04-30", 
        "2017-05-31", 
        "2017-06-30", 
        "2017-07-31"
    ], 
    "data1" : [
        14.44, 
        15.15, 
        14.84, 
        14.2
    ], 
    "data2" : [
        22.09, 
        22.55, 
        22.03, 
        21.24
    ], 
    "id" : NumberInt(34)
}
```

In this document, the final output required contains 4 variables, and 3 variables are store as array field. We can use the `unwind` and `project` operation to get the 4×4 table. The query code is 

``` js
// Requires official MongoShell 3.6+
use TEST_DB;
db.TEST_COLLECTION.aggregate(
    [
        { 
            "$unwind" : {
                "path" : "$date", 
                "includeArrayIndex" : "idx"
            }
        }, 
        { 
            "$project" : {
                "_id" : 0.0, 
                "date" : 1.0, 
                "id" : 1.0, 
                "data1" : {
                    "$arrayElemAt" : [
                        "$data1", 
                        "$idx"
                    ]
                }, 
                "data2" : {
                    "$arrayElemAt" : [
                        "$data2", 
                        "$idx"
                    ]
                }
            }
        }
    ], 
    { 
        "allowDiskUse" : true
    }
);
```

In stage 1, we unwind the `date` field, and it returns the `idx` indicates the index of the unwinded document in the field. With the idx, we can use `arrayElemAt` operation to access the corresponding value of other variables(i.e. `data1` and `data2`), then use `project` operation to the get the field. The final result is 

```json
{ 
    "date" : "2017-04-30", 
    "id" : NumberInt(34), 
    "data1" : 14.44, 
    "data2" : 22.09
}
{ 
    "date" : "2017-05-31", 
    "id" : NumberInt(34), 
    "data1" : 15.15, 
    "data2" : 22.55
}
{ 
    "date" : "2017-06-30", 
    "id" : NumberInt(34), 
    "data1" : 14.84, 
    "data2" : 22.03
}
{ 
    "date" : "2017-07-31", 
    "id" : NumberInt(34), 
    "data1" : 14.2, 
    "data2" : 21.24
}
```

## 2. 1 array field × N obeservations × M variables case

In this case, the document is something like 

```json
{ 
    "_id" : ObjectId("5abdaecad1673e0af4ddff6c"), 
    "status" : NumberInt(0), 
    "message" : "Success", 
    "data" : {
        "totalJoinAmount" : "5201314.00", 
        "totalCount" : NumberInt(2), 
        "list" : [
            {
                "userId" : NumberInt(13), 
                "nickName" : "Lisa", 
                "amount" : NumberInt(2600657), 
                "createTime" : NumberLong(1473266281111), 
                "tradeMethod" : "PC", 
                "finalAmount" : NumberInt(0), 
                "ucodeId" : null
            },
            {
                "userId" : NumberInt(14), 
                "nickName" : "Ethan", 
                "amount" : NumberInt(2600657), 
                "createTime" : NumberLong(1473266280720), 
                "tradeMethod" : "MOBILE", 
                "finalAmount" : NumberInt(0), 
                "ucodeId" : null
            }
        ]
    }, 
    "id" : NumberInt(9999)
}
```

We have two obeservations, and each observation is stored as an element of the value of array field `list`. The method is as follows

+ use `project` to get the information we want.
+ use `unwind` to unwind the list.
+ use `project` to get the fields we need.
+ use `out` to store the output to another collection.

Here is the query code:

```js
use TEST_DB;
db.TEST_COLLECTION.aggregate(
    [
        { 
            "$project" : {
                "_id" : 0.0, 
                "status" : 1.0, 
                "message" : 1.0, 
                "totalJoinAmount" : "$data.totalJoinAmount", 
                "totalCount" : "$data.totalCount", 
                "list" : "$data.list", 
                "id" : 1.0
            }
        }, 
        { 
            "$unwind" : {
                "path" : "$list", 
                "includeArrayIndex" : "idx"
            }
        }, 
        { 
            "$project" : {
                "status" : 1.0, 
                "message" : 1.0, 
                "totalJoinAmount" : 1.0, 
                "totalCount" : 1.0, 
                "userId" : "$list.userId", 
                "nickName" : "$list.nickName", 
                "amount" : "$list.amount", 
                "createTime" : "$list.createTime", 
                "tradeMethod" : "$list.tradeMethod", 
                "finalAmount" : "$list.finalAmount", 
                "id" : 1.0, 
                "idx" : 1.0
            }
        }, 
        { 
            "$out" : "Ich Liebe Dich"
        }
    ], 
    { 
        "allowDiskUse" : true
    }
);
```

The final result (in `Ich Liebe Dich` collection) is 

```json
{ 
    "_id" : ObjectId("5ae664119b2215a5caffa0e4"), 
    "status" : NumberInt(0), 
    "message" : "Success", 
    "id" : NumberInt(9999), 
    "totalJoinAmount" : "5201314.00", 
    "totalCount" : NumberInt(2), 
    "idx" : NumberLong(0), 
    "userId" : NumberInt(13), 
    "nickName" : "Lisa", 
    "amount" : NumberInt(2600657), 
    "createTime" : NumberLong(1473266281111), 
    "tradeMethod" : "PC", 
    "finalAmount" : NumberInt(0)
}
{ 
    "_id" : ObjectId("5ae664119b2215a5caffa0e5"), 
    "status" : NumberInt(0), 
    "message" : "Success", 
    "id" : NumberInt(9999), 
    "totalJoinAmount" : "5201314.00", 
    "totalCount" : NumberInt(2), 
    "idx" : NumberLong(1), 
    "userId" : NumberInt(14), 
    "nickName" : "Ethan", 
    "amount" : NumberInt(2600657), 
    "createTime" : NumberLong(1473266280720), 
    "tradeMethod" : "MOBILE", 
    "finalAmount" : NumberInt(0)
}
```

## Reference

+ [Official unwind manual from MongoDB](https://docs.mongodb.com/manual/reference/operator/aggregation/unwind/index.html)
+ [MongoDB unwind multiple arrays](https://stackoverflow.com/questions/39373442/mongodb-unwind-multiple-arrays)
+ [Print nested json array values into csv using MongoDB](https://stackoverflow.com/questions/26252454/to-print-nested-json-array-values-into-csv-using-mongodb)
+ [MongoDB show children items in One to Many relationship](https://stackoverflow.com/questions/39426022/mongodb-show-children-items-in-one-to-many-relationship)

