# print middle character and last two characters
str = input("Enter a new value: ")
mid = len(str)//2
middlecharacter = str[mid-1: mid+2]
print(middlecharacter)
lastcharacter = str[-2: ]
print(lastcharacter)