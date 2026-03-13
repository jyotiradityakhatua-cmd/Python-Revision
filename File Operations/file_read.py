file = open("data.txt", "r")
content = file.read()
print(content)
file.close()



with open("data.txt", "r") as file:
    content = file.read()
    print(content)



file=open("ayushman.txt","r")
jyotir=file.read()
print(jyotir)
file.close()


with open("kunal.txt","r") as file:
    jyotir=file.read()
    print(jyotir)
