def gen():
    for i in range(100):
        yield i

    print(gen())

    for i in gen():
        print(i)

def gen():
    for i in range(10):
        yield i

print(gen())        

for i in gen():     
    print(i)






    def gen():
        for i in range(35):
            yield i

    print(gen())
        
    for i in gen():
        print(i)