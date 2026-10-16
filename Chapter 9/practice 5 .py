# Inherritance code

# Parent class
class Vehicle: 
    @staticmethod
    def start():
        print("vehicle is starting:")
class car(Vehicle):
        @staticmethod
        def drive():
            print("car is now moving:")   
class Bike(Vehicle):
        @staticmethod
        def ride():   
            print("bike is now travelling:")
class truck(Vehicle):
        @staticmethod
        def load():
            print("truck is fully loaded with the equipments")  

#create an object
c= car()
c. start()
c. drive()               
b= Bike()
b. start()
b. ride()
d= truck()
d. start()
d. load()
