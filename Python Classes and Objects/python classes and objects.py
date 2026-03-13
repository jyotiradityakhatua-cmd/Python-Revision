class student:
    color="geen"
    name="Jyotiraditya"
    age=21

s1=student()
print(s1.color)
print(s1.name)
print(s1.age)


class car:
    model="toyota"
    color="black"
    engine="b5"

m=car()
print(m.model)
print(m.color)
print(m.engine)



class jyotir:
    age=21
    hobby="game"
    system="mac"


class kunal:
    age=20
    hobby="coffee drinking"
    system="mac"


class ayush:
    age=12
    hobby="eating coffee"
    system="ubantu"


s1=jyotir()
print(s1.age)
s2=jyotir()
print(s1.hobby)
s3=kunal()
print(s3.age,s3.hobby)
s4=ayush()
print(s4.hobby)


class kunal:
    def __init__(self,f_name,grade):
        self.n=f_name
        self.g=grade

s1=kunal("Jyotiraditya","A")
print(s1.n)
print(s1.g)
