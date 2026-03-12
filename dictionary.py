my_set = {1, 2, 3, 4, 5}
print(my_set)

set2={1,2,3,4,5,6,7,8,9}
print(set2)

set3={"Jyotir","Kunal","Ayushman",9,4.5,True}
print(set3)


#Built in functions in set
#ADD
set2.add(0)
print(set2)
#remove
set2.remove(0)
print(set2)

#clear
set2.clear()
print(set2)

#pop
set3.pop()
print(set3)

#copy
set3.copy()
print(set3)

#difference
set3.difference()
print(set3)

#update
set2.update(set3)
print(set2)

#Union
set2.union(set3)
print(set2)

#Intersection
set3.intersection(set2)
print(set3)

for i in set3:
    print(i)
