# #here we will study the basics of the tuples 
# mytuple = (23,5,67,89)
# namestu = ("laiba", "heer khan", "saliha", "tanzeela","laiba","ayra khan", "ayra khan")
# print(len(namestu))
# print(namestu)

# print(namestu[1])

# #empty tuple
# emptytuple = ()
# print(type(emptytuple))
# print(type(mytuple))
# print(type(namestu))

# #single tuple
# singletuple = (6 ,) # so the difference between emptytuple and sinletuple is this if we use "," between them
# print(type(singletuple))
# print(mytuple.index(67,))
# print(namestu.index("heer khan"))
# print(namestu[3])
# print(namestu.count("ayra khan"))

# #tuple basics
my_tuple = (34, 'laiba', "ict" , 5.5, 3, 6.7)
# my_tuple[3] = 67 #by assigning a new value to tuple we can see that tuple are immutable
print(my_tuple) 

#the question is how we can print empty tuple
# empty_tuple = ()
print(type(my_tuple))
print("the index of the 2nd value of the tuple: ",my_tuple.index("ict"))
print("the value of the character if the value of the tuple: ", my_tuple[1].index("b"))#if you want to access a single chararcterr of any value of the tuple.
print("count the string 'laiba' is occured how many time in a tuple:", my_tuple.count("laiba"))
print("show the index 2 from tuple:",my_tuple[2])
print("show the index of index 2 from tuplr:",my_tuple[2][2])
print("length of the tuple:", len(my_tuple))
print("length of the single vavlue of the tuple:",len(my_tuple[1]))


