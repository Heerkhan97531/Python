# You must have a nested dictionary containing at least three products (e.g., laptop, smartphone, and headphones), where each product includes its price and stock quantity.

# Take input from the user to check which product they want to look up.

# Safely use the built-in dictionary method .get() to check if the product exists. If it does, print its details (price and stock); otherwise, show an appropriate warning or error message.

# Include a feature or function that allows the user to add a new product or update the price and stock of an existing product using the .update() method.

inventory = {
    "laptop": {"price": 60000, "quantity": 6},
    "smart phones":{"price": 65000, "quantity":5},
    "headphones":{"price": 20000, "quantity": 3}
    }
def check_stock_and_price():
    item = input("enter the item:  ")
    product = inventory.get(item)
    if product:
        print(f"Product: {item.capitalize()}")
        print(f"Price: Rs.{product["price"]}")
        print(f"Quantity: {product["quantity"]}")
    else:
        print("Item is not found:")

def changing_item():
    item = input("Enter a new product:")
    new_price = float(input("enter the price of the product:"))
    new_stock = int(input("enter the quantity of the new_product:"))

    inventory.update({"item" : {"price": new_price, "stock": new_stock}})
    print(f"\nSuccessfully updated! Current Inventory:\n{inventory}")

check_stock_and_price()
changing_item()