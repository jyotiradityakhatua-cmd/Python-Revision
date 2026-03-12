from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

cm = ChainMap(dict1, dict2)

print(cm['a'])  
print(cm['b'])  
print(cm['c']) 




kunal={1:"boy",2:"smart",3:"healthy"}
ayush={4:"man",5:"intelligent",6:"fit"}
cm=ChainMap(kunal,ayush)
print(cm[1])
print(cm[2])
print(cm[3])
print(cm[4])



raghav={1:"sam",2:"VIRAT",3:"KOHLI"}
MS={4:"mahendra",5:"singh",6:"Dhoni"}
cm=ChainMap(raghav,MS)
print(cm[1])
print(cm[2])
print(cm[5])
print(cm[6])