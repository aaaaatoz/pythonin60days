lst = [1, 3, 5]  # list 变量

tup = (1,3,5) # tuple 变量

dic = {'a':1, 'b':3, 'c':5} # a dictionary

s = {1,3,5} # a set

## common string operations
# - strip
# - join
# - replace
# - title
# - find



class Dog(object):
    def __init__(self, name, dtype):
        self.__name = name      #private property, can't be modified by assignment'
        self.__dtype = dtype

    @property           # convert name into a read-only property
    def name(self):
        return self.__name

    @property
    def dtype(self):
        return self.__dtype

    @dtype.setter
    def dtype(self, nametype):
        self.__dtype = nametype

    def shout(self):
        print('I\'m %s, type: %s' % (self.name, self.dtype))



wangwang = Dog('wangwang', 'cute_type')

print(wangwang.name)
print(wangwang.dtype)
wangwang.dtype = "a new type"
# wangwang.name = "not be able to set"
print(wangwang.dtype)
wangwang.shout()