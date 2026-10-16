# #Practice 1: Method 1# take a diameter as an input and also find the area of circle
import math
diameter = int(input("enter the value of diameter: "))
radius = diameter/2
area = math.pi*(radius**2) #if you don't have to import math library so you can use 3.141... value of the pi
print("the area of the circle:", area)

 #Practice 2: find the area of square
length = float(input("enter the value of length  "))
width = 5.7
area = length*width
print("the area of square: ", area)

#Practice 3: Method 1 #find the area of triangle
base = float(input("enter the value of the base of the triangle: "))
height = 4.5
area = 0.5 *base*height
print("the area of the triangle is : ", area)

# Method 2 #jab apko base aur height nh de gaye par ap ko teeno sides ki height ka pata h tu ous ke 
#leye ap ye method aur formula use karte hu jis ka name h Heron's Formula.
import math
a= 23
b= 45
c=12
s= a+b+c/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print("the area is = ",area)

#Practice 4: Method 1 #practice of the area of the rectangle
length = int(input("enter the value of the length of the rectangle: "))
width= int(input("enter the value of the width of the rectangle: "))
area = 0.5*length*width
print("the area of the rectangle is: ", area)

#Method 2 #Custom function bnna ke
#Agar aapko apne program me baar-baar area nikalna ho, toh ek "def "function bana sakte hain
def calculate_rectangle_area(length, width):
    return length*width
#call to the function
area1= float(calculate_rectangle_area(10.6,23.0))
area2= int(calculate_rectangle_area(3, 65))
# output
print("area 1",area1)
print("area 2",area2)

#Method3# Object Oriented Programming se
#Jab aap bada software banate hain, toh Class aur Object ka use karke area nikala jata hai
class Rectangle:
    def __init__(self,length, width):
        self.length= length
        self. width= width
    def get_area(self):
         return self.length * self.width   
#object create krne
rect= Rectangle(2.3,4.5)
print("oop ke zariyee area find karna ",rect.get_area())    