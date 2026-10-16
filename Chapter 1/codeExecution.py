name = "Ayra khan"
height = 5.3
age1 = 19
age2= 20
print ("Actual value: ", age2)

age2 = age1
print("changed value:",   age2)


#stuck and heap memory address
#shallow copy
x=20
y=x
print("x ki reference value:", id(x))
print("y ki reference value:", id(y))

#jab "x" variable ki value phir change kar de
#deep copy
x=40
print("x ki updated value:",id(x))
print("y ki updated value:",id(y))