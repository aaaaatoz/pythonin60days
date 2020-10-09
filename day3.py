empty = []
lst = [1, 'xiaoming', 29.5, '17312662388']
lst2 = ['001', '2019-11-11', ['三文鱼', '电烤箱']]

print(len(empty))
print(len(lst))
print(len(lst2))

for _ in lst:
    print(f'{_}的类型为{type(_)}')

sku = lst2[2] # sku 又是一个列表
sku.append('烤鸭')

print(sku)
print(lst2) # 应该有烤鸭

## 浅拷贝
a = [1,2,[3,4,5]]
ashallow = a.copy() # ashallow 获得了a的值，但是只有一层，第二层其实是'指针'
ashallow[0] = 0 #a不会变化
ashallow[2][0] = 6 # ashallow 中的【2】是个指针，所以改变了之后a也会相应变化

print(a)   # a
print(ashallow)

# 深拷贝
from copy import deepcopy
a = [1,2,[[3,4,5],6,7]]
adeep = deepcopy(a) # 深拷贝，完全拷贝了内容
adeep[2][0][1] = -1
print(a)
print(adeep)
#深拷贝后，对深拷贝对象的操作，和原来对象，毫无关系


