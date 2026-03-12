a=["Kunal","Jyotir","Ayushman"]
b=[1,34,23,12,89,6,75,43,31,7,9]
c=[12.4,778,90.6,2.5,56,7,12.5,True]
print(a,b,c)

a[2]=9
print(a)

a[-1]=0
print(a)

print(a[::-1])
print(a[1:3])

#Concatenation
print(a+b)
print(a+b+c)

#Repetation
rep = a*4
print(rep)

#Membership
# in -> membership ficntion

# 3 in [1,2,3] = True0

if 3 in [1,2,3]:
    print('hola')


#methods
a.append(4)
print(a)

b.sort()
print(b)

b.reverse()
print(b)

b.sort(reverse=True)
print(b)

b.insert(7,[0])
print(b)

b.insert(3,5)
print(b)

b.remove(75)
print(b)

b.remove(34)
print(b)

b.clear()
print(b)

c.copy()
print(c)

c.pop()
print(c)

c.pop(5)
print(c)

a.pop(2)
print(a)

a.extend(c)
print(a)

#loop
for i in a:
    print(i)


#deleting in list
del c[1]
print(c)



thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  




fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)







jyotir=["star","moon","earth","jupiter"]
x=[]

for b in jyotir:
   if "a" in b:
      x.append(b)
      print(x)



jyotir=["star","moon","earth","jupiter","saturn"]


x=[z for z in jyotir if "a" in z]

print(x)
