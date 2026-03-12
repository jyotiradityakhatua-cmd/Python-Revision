from collections import Counter
a=["a","a","b","c","b","d","e","d"]
c=Counter(a)
print(c)


a="Jyotiraditya"
c=Counter(a)
print(c["J"])
print(c.most_common(3))

a=["a","a","b","c","b","d","e","d"]
c=Counter(a)
print(c.most_common(2))


a="Jyotiraditya"
c=Counter(a)
print(c["J"])


from collections import Counter

c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 + c2)


a="Jyotiraditya"
c=Counter(a)
del c[a]
print(c)
print(c.most_common(3))


a=["a","a","b","c","b","d","e","d"]
c=Counter(a)
c.update("m")
print(c)
print(c.most_common(2))