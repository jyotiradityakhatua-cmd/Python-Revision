from collections import OrderedDict
od=OrderedDict()
od["a"]=1
od["b"]=2
od["c"]=3
od["d"]=4
print(od)
for key, value in od.items():
    print(key,":",value)


from collections import OrderedDict
od=OrderedDict()
od["a"]=5
od["b"]=6
od["c"]=7
od["7"]=8
print(od)
for key, value in od.items():
    print(key,";",value)



