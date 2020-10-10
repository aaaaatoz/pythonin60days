# list tuple 操作

mylist = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 1]
mytuple = (1,2,3,4,5,6,1,2,3,4,1)

print(mylist.count(1))

print(mytuple.count(5))

# reverse the list or tuple

print(mylist[::-1])
print(mytuple[::-1])

# 获得最大值，获得出现最多次数值
print(max(mylist))
print(max(mylist, key = lambda v: mylist.count(v)))

print(list(zip([1,2],[3,4])))


# 随机数和洗牌
from random import randint, sample, shuffle
lst = [randint(0, 50) for _ in range(100)]  # randint 生成随机整数；
print(lst)
lst_sample = sample(lst, 10)  # sample 从 lst 中抽样 10 个元素
print(lst_sample)

shuffle(lst)
print(lst)

