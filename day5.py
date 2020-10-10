# dict 操作
# 创建

mydict1 = {'a':1,'c':3,'e':5}
mydict2 = dict(a=1,b=2,c=3)
mydict3 = {}.fromkeys(('a','b','c'), 1)

print(mydict1)
print(mydict2)
print(mydict3)

# 遍历字典
for key, val in mydict1.items():
    print(key, val)


# 获取
print(set(mydict1))
print(set(mydict3.keys()))

# 获取字典的值
print(list(mydict3.values()))

# 看字典中是否存在元素
print('e' in mydict3)

# 获取元素，并提供一个默认值
print(mydict3.get('a', None))

# 擅长元素
del mydict1['a']
print(mydict1)

mydict2.pop('a')
print(mydict2)

# 字典视图
mydict = {'a':1, 'b':2, 'c': 3}
mydict_keys = mydict.keys()
mydict_values = mydict.values()
mydict_items = mydict.items()

print(mydict_items)
print(mydict_keys)
print(mydict_values)

# 改变原有字典，会修改字典视图
mydict['a'] = '-1'
mydict['d'] = 4

print("after dictionary changed")
print(mydict_items)
print(mydict_keys)
print(mydict_values)


# set集合操作
myset1 = {1,2,3}
myset2 = set([1,2,4])
myset = {1,2}

# 集合并
print(myset1.union(myset2))
# 集合差
print(myset1.difference(myset2))
# 集合交集
print(myset1.intersection(myset2))

# 集合子集
print(myset.issubset(myset1))

# 集合超集
print(myset2.issuperset(myset))
