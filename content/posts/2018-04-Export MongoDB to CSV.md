---
title: Export from MongoDB to csv
date: '2018-04-13'
author: Dongsheng Deng @
slug: export from mongodb to csv
draft: false
categories:
  - Python
tags:
  - Python
  - MongoDB
  - JSON
---

## 1. Use MongoDB to save json file
When scraping data from web, the response may be json format, we can use `json` library to handle this.

```python
import requests
import json
import pymongo

# start pymongo
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

When the field is a dict, then you can treat the key-value pair as a subfield, and export as the normal field (length of 1). However, sometimes the filed of the json file contains a array, moreover, you need to convert the field array to rows of a table (ie, observations), and convert the field name to the header of the table (ie, variable name). 

## 2. Convert non-regular json to normal for exporting
For instance, the following json (from MongoDB) is not in the regular format, we cannot do much to the json (map reduce, aggregate, pipline operation etc.), we need convert it to normal table, export to csv/table or re-dump into MongoDB.

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

or the origin dictionary looks like

```python
long_dict = {
    "date" : {
       "1":"2017-04-30", 
       "2":"2017-05-31", 
       "3":"2017-06-30", 
       "4":"2017-07-31"
    }, 
    "data1" : {
       "1":14.44, 
       "2":15.15, 
       "3":14.84, 
       "4":14.2
    }, 
    "data2" : {
       "1":22.09, 
       "2":22.55, 
       "3":22.03, 
       "4":21.24
    }, 
    "id" : 34
}
```

The expected result is 

<center><img src="/posts/image/expected.png" width=350,alt="expected result" /></center>

The code is as follows

```python
import json 
import pandas as pd

# 1. dump dict to json string, and loads to get json type.
result_json = json.loads(json.dumps(long_dict))

# 2. convert the json to pandas data frame.
result_df =pd.DataFrame.from_records(result_json)

# 3. convert the data frame to dict using to_dict method with argument "records".
# 4. insert all the records to MongoDB.
db_test.insert_many(result_df.to_dict('records'))
```

**Tips**: The old MongdoDB document turns 4 documents in this example. If you want to export to csv, you can use previous command `mongoexport`.


## Reference 

+ [Convert dictionary to json in python](https://stackoverflow.com/questions/26745519/converting-dictionary-to-json-in-python)
+ [Convert json to pandas dataframe](https://stackoverflow.com/questions/21104592/json-to-pandas-dataframe)
+ [Insert pandas dataframe into mongodb using pymongo](https://stackoverflow.com/questions/20167194/insert-a-pandas-dataframe-into-mongodb-using-pymongo)


