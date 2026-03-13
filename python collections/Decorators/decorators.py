#A decorator is a function that modifies the behavior of another function or class without permanently changing it. It’s like wrapping a gift: you don’t change the gift itself, but you change how it looks or behaves when presented.



def my_decorator(func):
    def wrapper():
        print("Jyotiraditya")
        func()
        print("jyotir") 
    return wrapper
    
@my_decorator
def say_hello():
    print("hello")

say_hello()
    

def my_decorator(func):
    def wrapper():
        print("jyotir")
        func()
        print("kunal")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()




def my_decorator(func):
    def wrapper():
        print("Ayush")
        func()
        print("Kunal")
    return wrapper


@my_decorator
def say_hello():
    print("hello")

say_hello()
