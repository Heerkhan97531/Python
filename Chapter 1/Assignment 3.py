#Problem Statement / Requirements:

# User se Total Bill Amount puchhein (float).

# Tip percentage puchhein (e.g., 10, 12, ya 15%).

# Kitne log bill split kar rahe hain unki tadad puchhein (int).

# Total bill mein tip add karke har shakhs ke hissey mein aane wali exact amount
# calculate karein aur result ko 2 decimal places tak round() karke display karein.

print("----WELLCOME TO THE SMART BILL SPLITTER----")
#inputing the values
total_bill = float(input("Enter the amount of total-bill RS :"))
tip_percentage= float(input("Enter the percentage of the tip : "))
person = int(input("Enter the number of the persons: "))

#Calculation
total_tip =  total_bill * (tip_percentage/100)
final_result = total_tip + total_bill
per_person = final_result/person

#output
print(f"total bill with tip: RS {round(final_result , 2)}")
print(f"per person share: RS {round(per_person , 2)}")
      
