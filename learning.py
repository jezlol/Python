from collections import namedtuple

a = namedtuple('courses', 'name, technology')
s = a._make(['artifinial intelligence', 'python'])
print(s)