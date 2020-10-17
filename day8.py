# 内置函数
# 类型函数
print(bool(1))
print(bool(0))

print(str(123))
print(str([123,345]))

print(dict(a='a',b='b'))
print(dict([('a',1),('b',2)]))

#int - 转化成int 或者 抛出 ValueError
print(int('123'))

#
print(frozenset([1,2,3,4,3,21]))

#
myset = {1,2,3}
myset.add(4)
print(myset)
myset.pop()
print(myset)

#
print(list(myset))

#
mytuple=tuple([1,2,3])
print(mytuple)


# zip
a = range(5)
b = list('abcde')
for x,y in zip(a,b):
    print(x,y)