a=[1,2,3,4,5,6,7,8,9]
j=map(lambda x: x**2,a)
print(list(j))


b=[2,3,4,5,6,7,8,9]
a=map(lambda x:x**2,b)
print(list(a))


c=(9,6,4,7,3,1)
c=filter(lambda x:x %2==0,c)
print(tuple(c))


a=[8,7,9,2,56,4,12]
a.sort(key=lambda x:x)
print(a)


c=[67,23,12,4,99,65]
c.sort(key=lambda x:x)
print(c)