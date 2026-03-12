def add(a,b):
    sum=a+b
    print(sum)
    return sum
add(2,3)
add(6,7)
add(9,8)

def substract(a,b):
    minus=a-b
    print(minus)
    return minus
substract(8,3)
substract(12,6)


def multiplication(a,b):
    multiply=a*b
    print(multiply)
    return multiply

multiplication(1,6)
multiplication(6,9)


def division(a,b):
    divide=a/b
    print(divide)
    return divide
division(6,2)

#default parameters
def add(a,b=6):
    sum=a+b
    print(sum)
    return sum

add(3)

def add(b,a=6):
    sum=a+b
    print(sum)
    return sum
add(1)


def converter(usd_val):
    inr_val= usd_val*91
    print("USD" ,usd_val, "Inr",inr_val)
    return "USD" ,usd_val, "Inr",inr_val

converter(90)


def call_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(fact)

call_fact(7)


ayush=["yellow","blue","green","red","blue"]
kunal=["k","u","n","a","l"]

def lambai(list):
    print(len(list))
    return len(list)


lambai(ayush)
lambai(kunal)