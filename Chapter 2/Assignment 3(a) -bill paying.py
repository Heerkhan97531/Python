# total amount of bill $ no of friends
bill= float(input("Enter the total amount of bill: " ))
friends= float(input("Enter the number of friends: "))
pay= bill/ friends
print(" bill will be pay by each: ", pay)
print("Data type of vaiables:")
print("bill: ", {type(bill)})
print("friends:", {type(friends)})
print("pay: ", {type(pay)})