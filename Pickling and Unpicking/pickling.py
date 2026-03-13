
#pickling

import pickle

a={1:"Jyotir",2:"Ayushman",3:"Kunal"}
with open("a.pkl","wb") as file:
    pickle.dump(a,file)

import pickle

data = {"name": "Kunal", "age": 20, "skills": ["Python", "Java"]}
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)  

import pickle

data={"name":"jyotir","age":21,"sub":"python"}
with open("data.pkl","wb") as file:
    pickle.dump(data,file)


s=["jyotir","ayushman","kunal"]
with open("s.pkl","wb") as file:
    pickle.dump(s,file)