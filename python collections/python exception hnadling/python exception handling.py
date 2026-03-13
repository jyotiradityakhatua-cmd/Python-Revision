#Python exception handling

#Exception handling in Python is a way to catch and manage errors that occur at runtime so your program doesn’t crash unexpectedly.




try:
    x=10/0

except ZeroDivisionError:
    print("this number is can not divided by 0")



try:
    num=int(input("enter the number:"))
    x=10/num
    print("result",x)


except ZeroDivisionError:
    print("it can not divided by 0")

except ValueError:
    print("invalid input")




try:
    num=int(input("enter the number:"))
    x=10/num

except ZeroDivisionError:
    print("the number can not divided by zero")

else:
    print("no error occured")

finally:
    print("this always run","cleanup here")

