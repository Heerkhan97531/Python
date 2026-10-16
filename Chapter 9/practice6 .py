# Polymorphism Method in oop

class Dog:
    def sound(self):
        print("Dog says: Bark")
class cat:
    def sound(self):
        print("cat asys: meow")
class cow:
    def sound(self):
        print(" cow says: moo")

animals = [Dog(), cow(), cat()]
for a in animals:
 a.sound()



# Example 2
class circle:
    def area(self):
        print("\n Area= 3.14*r*r")
class square:
    def area(self):
        print("area: side*side")
class rectangle:
    def area(self):
        print("area= length*width")
shapes= [circle(), rectangle(), square()]        
for s in shapes:
    s.area()