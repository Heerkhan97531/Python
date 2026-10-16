# #take input to show is it positive or negative
# num = 0
# if (num>0):
#    print("The number is positive:")
# elif(num<0):
#    print("the number is negative:")
# else:
#     print("the number is zero")



# #Practice #01
# n = 30
# if n>40:
#    print("Class 'A' ")
# elif n>20:
#    print("Class 'B'")
# elif n>10:
#    print("Class 'C'")
# elif n>30:
#    print("Nothing TRUE...")
 #(here it's answer is Class B . the reason behind this is that firstly compiler checkout the first if condition
 # and see that condition doesn"t true because "n " numbe is not greater than 40 and then the compiler move on toward next
 # satement an dyiui csn see the condition is true because "n" number is greater than 20 so it prints it. The compilere will 
 # not move to the next statement.)


#Find out the score:
score = 70
if score>80:
   Grade = 'A'
if score>69:
   Grade = 'C'
if score>50:
   Grade = 'B'
print("Grade of the student: ",Grade) # here are two ways of storing vaues into the progrms the first is the 
# method in which you can directly print a statement when the program runs and the condition true and the second side is that 
# you can craete a new varaible at each condition and at the end of the conditions it will be print.     

#Practic a queston by taking input from the user and the secind thing id that to create different variables at each condtiion to check out
x = int(input("Enter any number: "))
if x>0:
   number = x
   print("positive: ",number)
elif x<0:
   number = -x
   print("Negative: ",-number)
else :
   number = 0 
   print("the number is zero: ",number)
