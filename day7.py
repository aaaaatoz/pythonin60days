# common functions

#len
dic = {'a':3,'b':1}
mylist = [1,2,3,4,5]
mytuple = (1,2,3,4,5)
myset = {1,2,3,4,5}

print(len(dic))
print(len(mylist))
print(len(mytuple))
print(len(myset))

#max
print(max(dic)) # max on the key
print(max(mylist))
print(max(mytuple))
print(max(myset))



def max_length(*lst):
    return max(*lst, key=lambda v: len(v))

max_length([1, 2, 3], [4, 5, 6, 7], [8])

# pow(x, y, z=None, /)
# x 为底的 y 次幂，如果 z 给出，取余：

print(pow(2,3))
print(pow(2,3,5))

# round(number[, ndigits])
#四舍五入，ndigits 代表小数点后保留几位：
print(round(10.2345, 3))

# sum(iterable, /, start=0)
# 求和：

a = [1,4,2,3,1]
print(sum(a))

#  abs(x, /)
print(abs(-55))

# divmod(a,b) 同时返回商和余数
print(divmod(43, 5))

# hash(object)　　
# 返回对象的哈希值：
#
# id(object)　　
# 返回对象的内存地址：

# all(iterable)
# 接受一个迭代器，如果迭代器的所有元素都为真，返回 True，否则返回 False：
print(all([1,0,3,6]))
print(all([1,2,3]))

# any(iterable)　
# 接受一个迭代器，如果迭代器里有一个元素为真，返回 True，否则返回 False：
print(any([0,0,0,[]]))
print(any([0,0,1]))
