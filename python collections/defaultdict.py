from collections import defaultdict
dd = defaultdict(int)

dd['a'] += 1
dd['b'] += 2

print(dd)


from collections import defaultdict
dd=defaultdict(int)
dd["a"]+=1
dd["b"]+=2
dd["c"]+=3

print(dd)


from collections import defaultdict
dd=defaultdict(list)
dd["jyotir"].append("apple")
dd["kunal"].append("mango")
dd["ayush"].append("papaya")
print(dd)

dd_custom = defaultdict(lambda: 'chhota bheem')

print(dd_custom['x']) 

nested_dd = defaultdict(lambda: defaultdict(int))
nested_dd['a']['x'] += 1
nested_dd['a']['y'] += 2

print(nested_dd)
