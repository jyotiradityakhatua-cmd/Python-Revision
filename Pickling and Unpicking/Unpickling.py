
import pickle

d=["Kunal","Ayushgman","jyotir"]
with open("d.txt","rb") as file:
    m=pickle.load(file)
    print(m)



data=["ayushman","kunal","jyotir"]
with open("data.txt","rb") as file:
    print(pickle.load(file))