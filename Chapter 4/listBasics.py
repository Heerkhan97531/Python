#print list in python  (Indexing and Length concept)
items = ["apple", "pizza", 5.3, "heer khan ",19, 'A', "cake"]
print("the lenght of the items: ",len(items))

#Double indexing to take character of any item of the list , we can use the concept of inedxing
print("enter the third item of the data:", items[3][2])

#indexing
print(items[3:7])



#Agar aap ko list ke andar maujood kisi ek item (jaise index 0 par maujood String) ki length pata karni hai,
#  toh aap len() ke andar double indexing wale andaaz mein hi us item ka reference de sakti hain:
my_list = ["Aira", 20, "ICT Course", 5.5]

# Index 0 par "Aira" hai
print(len(my_list[0]))  
# Output: 4 (Kyunki A-i-r-a mein 4 characters hain)

# Index 2 par "ICT Course" hai
print(len(my_list[2]))  
# Output: 10 (ICT = 3, Space = 1, Course = 6 -> Kul 10 characters space ke saath)

#Agar aap chahti hain ki list ki tamam values, un ke darmiyan ki spaces, commas (,) aur brackets
#  ([]) bhi gine jayein (yaani bilkul waise hi jaise woh screen/terminal par print hote hain), t
# oh aap poori list ko str() function ke zariye string mein badal kar us ki length nikal sakti hain:
my_list = ["Aira", 20, "ICT", 5.5]

# List ko mukammal Text/String mein badalna
list_as_string = str(my_list)

print(list_as_string)
# Output screen par: ['Aira', 20, 'ICT', 5.5]

# Ab is poore text ke ek ek character, comma, quotes, space aur bracket ko gina jayega
print(len(list_as_string))
# Output: 25

#Agar aap chahti hain ki brackets ya commas na gine jayein, balki har item ke apne characters ki total length ko aas paas mein add kar liya jaye, 
# toh Python mein sum() aur Loop ke zariye yeh kaam bhi ho sakta hai:
my_list = ["Aira", 20, "ICT", 5.5]

# Tamam data types (har number aur float) ko string mein badal kar un ke characters ginna
total_characters = sum(len(str(item)) for item in my_list)

print("all of the characters of each item:", total_characters)
# Breakdown:
# "Aira" = 4
# "20" = 2
# "ICT" = 3
# "5.5" = 3
# Total = 4 + 2 + 3 + 3 = 12

#to check that list is immutable
list = [45, "laiba", 'Python Developer', 5.5, 3, 'O']
print(list)
list[3] = 5.2
print(list)
