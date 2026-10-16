
# --- Global Variable ---
# Library ki inventory jisme kitabon ke naam aur unka stock hai
library_inventory = {
    "Python Programming": 4,
    "Data Science Basics": 2,
    "Web Development": 5
}

# Function 1: Kitab ki availability check karne ke liye (Return Statement ka use)
def check_book_availability(book_name):
    # Check karte hain ki kitab inventory mein hai aur stock 0 se zyada hai ya nahi
    if book_name in library_inventory and library_inventory[book_name] > 0:
        return True
    else:
        return False

# Function 2: Late fine calculate karne ke liye (Default Argument: fine_per_day = 10)
def calculate_fine(days_late, fine_per_day=10):
    if days_late <= 0:
        return 0
    
    basic_fine = days_late * fine_per_day
    
    # Agar 7 din se zyada deri ho, toh 50 rupay ki extra penalty jude gi
    if days_late > 7:
        extra_penalty = 50
        total_fine = basic_fine + extra_penalty
    else:
        total_fine = basic_fine
        
    return total_fine

# Function 3: Kitab issue ya return karne ke liye (Global Scope & Keyword Arguments)
def issue_or_return_book(action, book_name):
    # Global variable ko function ke andar modify karne ke liye 'global' keyword ka use
    global library_inventory
    
    action = action.lower()
    
    if action == "issue":
        # Function 1 ko call karke check kar rahe hain ki kitab available hai ya nahi
        if check_book_availability(book_name):
            library_inventory[book_name] -= 1
            print(f"Success: '{book_name}' successfully issue ho gayi hai! Bacha hua stock: {library_inventory[book_name]}")
        else:
            print(f"Sorry: '{book_name}' filhal library mein available nahi hai.")
            
    elif action == "return":
        if book_name in library_inventory:
            library_inventory[book_name] += 1
            print(f"Success: '{book_name}' wapas mil gayi hai. Updated stock: {library_inventory[book_name]}")
        else:
            library_inventory[book_name] = 1
            print(f"Success: Nayi kitab '{book_name}' library mein add kar di gayi hai.")
    else:
        print("Invalid action! Kripya 'issue' ya 'return' specify karein.")

# --- Program Testing / Function Calling ---
print("--- Initial Library Inventory ---")
print(library_inventory)
print("\n--- Library Operations ---")

# Keyword arguments ka istemal karke function call kar rahe hain
issue_or_return_book(action="issue", book_name="Python Programming")

# Fine calculate karne ka function call
late_days = 9
fine_amount = calculate_fine(days_late=late_days)
print(f"Kitab {late_days} din late lautane par fine bana hai: Rs. {fine_amount}")

# Kitab wapas (return) karne ka function call
issue_or_return_book(action="return", book_name="Python Programming")

print("\n--- Final Library Inventory ---")
print(library_inventory)