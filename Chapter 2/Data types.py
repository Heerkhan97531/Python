name= "Husna"
age= 19
height= 5.2
print (type(age))
print (type(name))

name = "Ayra khan"
marks= 78.97
age = 20
print(type(name))
print(type(age))
# print(type(marks))

#print out the age as an nput and sow it's value on the screen
age = int(input("take age as an input:"))
print("the age of the student is:",age, type(age))

#enter your favourite subject from the student and we will check that student ds elligible for our rcourse or not
favsubject = ["programming", "python", "machine learning", "data science"]
user_input = input("Enter your favourite subject from the list: ")
cleaned_data = user_input.lower()
print("Please confirm that your subject is = ", user_input)
if cleaned_data in favsubject:
    print("Congratulations! You have chosen the right subject",)
else:
    print("Sorry! You have chosen the wrong subject")    