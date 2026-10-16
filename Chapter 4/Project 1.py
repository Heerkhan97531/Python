#-------Python Project---------
print("\n-----Smart E-COMMERCE Discount and Cart Management---------\n")

cart_items =[1500, 300,600,3400,1200]
print("Initial cart items: " ,cart_items)
discount_rate = (10, 20)

age = int(input("Enter the age of the customer: "))
student_input= input("Are you a student? (yes/no): ").strip().lower()
is_student = (student_input == "yes" )  
Total_value = sum(cart_items) 
print("the total amount that you will pay is: ",Total_value)


if Total_value >5000 and is_student:
    discount_amount = Total_value *(discount_rate[0]/100)
    final_amount = Total_value-discount_amount
    print(f" 20% percent discount will be apply: -RS.{discount_amount}")
    print("Final Payment Amount is: RS.", final_amount)
elif Total_value>3000 and not is_student:
    discount_amount = Total_value *(discount_rate[1]/100)
    final_amount = Total_value - discount_amount
    print(f"10% percent discount will be apply:  -RS.{discount_amount}") 
    print("Final Payment Amount is : ", final_amount)
else:
    print("NO discount apllicable. ")
    print("Final Payment amount : RS.", Total_value)
    

print("\n -----Cart Operation-----\n")
length_item = len(cart_items)
print("Total number of items: ", length_item)
cart_items.append(499)
print("updated cart_items: ", cart_items)
print("Count the apperrance of that item which price is 600: ",cart_items.count(600))
