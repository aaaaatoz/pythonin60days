# dict

mydict = {"a":1, "b":2}
mydict.update({"a":-1, "c": 3, "d": 4})

print(mydict)

# setdefault
mydict.setdefault('e', 5)
mydict.setdefault('a', 999)

print(mydict)

#
def merge(d1, d2):
    return {**d1, **d2}
print(merge({'a': 1, 'b': 2}, {'c': 3}))

#
def difference(d1, d2):
    return dict([(k, v) for k, v in d1.items() if k not in d2])
print(difference({'a': 1, 'b': 2, 'c': 3}, {'b': 2}))

#
def sort_by_key(d):
    return sorted(d.items(), key=lambda x: x[0])

def sort_by_value(d):
    return sorted(d.items(), key=lambda x: x[1])

print(sort_by_key({'a': 3, 'b': 1, 'c': 2}))

#
def max_key(d):
    if len(d) == 0:
        return []
    max_key = max(d.keys())
    return (max_key, d[max_key])
print(max_key({'a': 3, 'c': 3, 'b': 2}))

def max_value(d):
    if len(d) == 0:
        return []
    max_value = max(d.values())
    return [(key, max_value) for key in d if d[key] == max_value]

print(max_value({"a":3, "b": 2, "c": 3, }))







