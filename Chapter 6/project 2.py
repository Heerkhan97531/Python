print("=======Inventory Stock & Price Validation Tool (E-Commerce Management)=======")

product = ["book" , "pen"," bootle","notes", "uniform"]
stock_num = [12,0, 5,20,13]
prices = [30000 , 2000, 4000, 1200, -14000]

for prod, sto_num, price in zip(product, stock_num, prices):
    print(f"product :{prod}  |  stock_num :{sto_num}  |  prices :{price}")

list = [stock_no < 5 for stock_no in stock_num]
print("these products are out of stock",list) 

for price in prices:
    if price <=0:
        print(f"skppind invalid data: this {product} prices {prices} is invalid ")
        continue
else:
    print(f"verified product {product} price {prices} is:")

print("\n--- 4. Break aur Else Loop (Critical Out-of-Stock Check) ---")
for name, stock in zip(product, stock_num):
    if stock_num == 0:
        print(f"CRITICAL ALERT: '{product}' ka stock 0 hai! Loop break ho gaya.")
        break
else:
    print("Sare valid products ka stock check ho gaya, koi critical emergency nahi hai.")    
