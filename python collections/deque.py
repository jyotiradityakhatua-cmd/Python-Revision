from collections import deque

d = deque([1, 2, 3])
d.append(4)
print(d)

d.appendleft(5)
print(d)

d.pop()
print(d)
  

d.popleft()
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)


from collections import deque

j = deque([7,9,2],maxlen=4)

j.append(5)
print(j)
j.appendleft(10)
print(j)
j.pop()
print(j)
j.popleft()
print(j)
j.rotate(1)
print(j)
j.rotate(-1)
print(j)

