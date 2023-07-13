from collections import deque

a = ['e','d','u','r','e','k','a']
d = deque(a)
#d.appendleft to show python on the left
d.pop()
print(d)

#d.popleft to remove value on the left
d.append('python')
print(d)