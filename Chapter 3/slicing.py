# #slicing practice
# str ="malayepizza"

# firsthalf = str[:6]
# secondhalf = str[3:8]


# print(firsthalf)
# print(secondhalf)
# print(str[ : ])

# # favourite food cake
# str = "Red valvet cake"
# middlecharacter = str[5:8]
# lastcharacter = str[10 : ]
# trail = str[13 : 15]

# print(middlecharacter)
# print(lastcharacter)
# print(trail)

# str = "Laiba Shahzadi"
# print(str[-9:-6])
# print(str[12:])

string = (input("enter the value:"))
mid = len(string)//2 #the double backward space is used to elminate 
#the floting part of the output means the number comes after decimal
characters = string[mid-1:mid+2]
print(characters)
string_2 = "Laiba Shahzadi"
print(string_2[-2:])