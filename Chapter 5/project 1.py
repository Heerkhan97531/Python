# create a dictonary storing meaning of 3 english words
meaning = {"dear": "payara",
           "discipline": "mustakil",
           "loyal" : "wafadar"}
print(meaning)

#create a set of numbers and show union and  of these numbers
num1= {2,4,6,8}
num2 = {3,4,5}
set1= num1.union(num2)
print(set1)

#create a set of numbers and show intersection and  of these numbers
num1 = {7, 8,9,0,4}
num2 = {2,4,6,8,7,4,1}
set2= num1.intersection(num2)
print(set2)

#add integer and float into the set and show what happened?
add ={9,9.0 , "burger"}
print(add)
print(len(add))
print(type(add))