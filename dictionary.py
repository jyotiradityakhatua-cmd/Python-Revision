dict_1={
        1:"hello",
        2:"This is me",
        3:"Jyotir"
}
print(dict_1)

dict_2={
1:"YASH",
"AGE":23,
"COURSE":"PYTHON"
}
print(dict_2)
print(dict_1[1])
print(dict_1[3])

for key in dict_1:
    print(key) 


1	#dict.clear()
#Removes all elements of dictionary dict

2	#dict.copy()
#Returns a shallow copy of dictionary dict

3	#dict.fromkeys()
#Create a new dictionary with keys from seq and values set to value.

4	#dict.get(key, default=None)
#For key key, returns value or default if key not in dictionary


5	#dict.items()
#Returns a list of dict's (key, value) tuple pairs

6	#dict.keys()
#Returns list of dictionary dict's keys



7	#dict.update(dict2)
#Adds dictionary dict2's key-values pairs to dict

8	#dict.values()
#Returns list of dictionary dict's values

for key, value in dict_1.items():
    print(key, value)

for k in dict_1:
    print(k,dict_1[k])


for m in dict_1.values():
    print(m)


        
        
        
        