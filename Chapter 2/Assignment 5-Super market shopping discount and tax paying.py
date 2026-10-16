print("-------🛒Super Market Shopping Discount & Tax Paying----------")
#User se Item 1 Price aur Item 2 Price input lein (String input ko float mein convert karein).

item_1 = float(input("enter the price of first item RS: "))
item_2 = float(input("enter the price of second item RS: "))

#Implicit conversion verify karne ke liye, quantity integer (e.g., x = 3) se multiply karein.

Quantity_1 = 20
print(type(Quantity_1))
Quantity_2 = 25
print(type(Quantity_2))
weightage_1 = item_1*20
print(type(weightage_1))
weightage_2 = item_2*25
print(type(weightage_2))
#Calculations:
# Total Cost = (Price1 + Price2)
# Tax Rate (5%) apply karein: 
# Tax Amount = Total Cost * 0.05  
# Grand Total = Total Cost + Tax Amount

total_cost = item_1 + item_2
print("the total cost of the items is RS:",total_cost)
tax_amount = total_cost *(5/100)
print("the taxAmount is RS: ",tax_amount)
Grand_total= total_cost + tax_amount
print("Amount that you will pay to the market: RS ",Grand_total)

#Assignment operator (+=) ka use karke packaging fee (50) Grand Total mein add karein.  
Grand_total+=50
#Comparison Operator ka use karke check karein: Kya Grand Total 1000 se zyada hai?
find = Grand_total>1000
print("the grand_total is greater than 1000 or not?",find)

