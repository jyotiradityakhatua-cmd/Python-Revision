class car:
    def start(self):
        print("car started")

class vehicle(car):
    def drive(self):
        print("driving car")

s1=vehicle()
s1.start()
s1.drive()



#multiple inheritance
class car:
    def start(self):
        print("car started")

class truck:
    pass

class cycle(car,truck):
    pass

s1=cycle()
s1.start()

#multilevel inheritance
class car:
    def start(self):
        print("car started")

class truck(car):
    pass

class cycle(truck):
    pass

s3=cycle()
s3.start()

#hierchial inheritance
class car:
    def start(self):
        print("car started")


class truck(car):
    pass

class tempo(car):
    pass

s5=tempo()
s5.start()


#hybrid contains the use of any two types of inheritance








