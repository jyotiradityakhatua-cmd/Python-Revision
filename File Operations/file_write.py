file=open("ayushman.txt","w")
s=file.write("hello")
print(s)
file.close()


with open("ayushman.txt","w") as file:
    s=file.write("namaste")
    print(s)
    

file=open("kunal.txt","w")
m=file.write("i am kunal")
print(m)
file.close()

with open("kunal.txt","w") as file:
    l=file.write("maggie")
    print(l)
    