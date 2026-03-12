fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


jyotir=["virat kohli","rohit sharma","ms dhoni"]
ayush=[]
for x in jyotir:
  if "o" in x:
    ayush.append(x)
    print(ayush)


numbers=[1,2,3,4,5]
vk=[]
for l in numbers:
  vk.append(l**2)
  print(vk)

  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
  newlist = []
  c = [x for x in fruits if "a" in x ]
  print(c)


word = "python"
letters = [char.upper() for char in word]
print(letters)

#nested comprehension
table = [[i*j for j in range(1,4)] for i in range(1,4)]
print(table)