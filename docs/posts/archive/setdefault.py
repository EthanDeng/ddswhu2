
# 字典的 setdefault 方法的用途是给一个字典某个 key 指定默认的 value
# 在 key 不存在的时候，会新建 key-value 对
# 但是当 key 存在的时候，setdefault 不会更改这个 key 所对应的 value。

spam = {'Name': 'Runoob', 'Age': 7}

spam.setdefault('Age','25')
spam.setdefault('Sex', 'NA')
spam.setdefault('School')

print ("Age 键的值为 : %s" % spam['Age']) #  Age 键存在在字典中，则不会设置 Age=25
print ("Sex 键的值为 : %s" % spam['Sex']) # Sex 键不存在，所以 Sex 会被指定为 NA
print ("School 键的值为 : %s" % spam['School']) # School 键不存在，不指定值，默认为 None
spam['Sex']="Female"
print ("新字典为：", spam)



