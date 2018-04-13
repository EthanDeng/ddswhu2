---
title: Export MongoDB to csv
date: '2018-04-14'
author: Dongsheng Deng @
categories:
  - Python
tags:
  - Python
  - MongoDB
  - JSON
---

## 1. store json file to MongoDB
When scraping data from web, the response may be json format, we can use `json` library to handle this.

```python
import requests
import json
import pymongo


connection = pymongo.MongoClient()
data_base = connection.data_base
collection = data_base.collection

response = requests.post(url=url, data=payload, headers=headers)

if response.status_code == 200:
    result_json = response.json()
    collection.insert(result_json)
```

If the json file is in right format, then you can use `mongoexport` command to export to csv.

```shell 
mongoexport --db data_base --collection collection --type=csv --fields field1,field2,field3, --out "D:\output.csv"
```

However, sometimes the filed of the json file contains a array, moreover, you need to convert the field array to rows of a table (namely, observations), and convert the field name to the header of the table (ie, variable name). When the field is a dict, then you can treat the key-value pair as a subfield, and export as the normal field (length of 1).

## 2. Convert non-regular json to normal json

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



## Reference 

+ [Convert json to pandas dataframe](https://stackoverflow.com/questions/21104592/json-to-pandas-dataframe)
+ [Insert pandas dataframe into mongodb using pymongo](https://stackoverflow.com/questions/20167194/insert-a-pandas-dataframe-into-mongodb-using-pymongo)


