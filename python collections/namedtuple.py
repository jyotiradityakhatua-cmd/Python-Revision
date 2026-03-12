from collections import namedtuple
student1 = namedtuple('student1',['name','rollno', 'marks'])
var = student1(name = 'Sai',rollno=237, marks=89)
print("Name :",var.name)
print("Rollno :",var.rollno)
print("Marks :",var.marks)



from collections import namedtuple
jyotir=namedtuple("jyotir",("name","age","job"))
j=jyotir("Jyotiraditya","22","Trainee")
print(j.name)
print(j.age)
print(j.job)

from collections import namedtuple
Kunal=namedtuple("Kunal",("name","age","job"))
K=Kunal("Ayushman","22","Asset")
print(K.name)
print(K.age)
print(K.job)


from collections import namedtuple
Jyotir=namedtuple("Jyotir",("degree","duration","branch"))
j=Jyotir("Kunal","23","Inten")
print(j.degree)
print(j.duration)
print(j.branch)