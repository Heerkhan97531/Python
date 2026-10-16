#Program 3: Account Username & Masked ID Generator
#(Mini Security Tool)
#Scenario: Jab aap kisi website ya bank app par login karte hain, toh safety ke liye aapka Full Name process karke 
#ek Unique Username aur Masked Email/ID banaya jata hai.
#User se unka Full Name (e.g., Amit Sharma) aur Phone Number (e.g., 9876543210) input lo.
#Username Banayein (Concatenation + Slicing): Name ke pehle word ke initial 3 letters aur phone number ke last 4 digits ko jodkar ek unique username banayein.
#Username Banayein (Concatenation + Slicing): Name ke pehle word ke initial 3 letters aur phone number ke last 4 digits ko jodkar ek unique username banayein.
# Masked Phone Number Banayein (Indexing + Slicing): Phone number ke pehle 6 digits ko * se replace karein 
# aur sirf last 4 digits dikhayein.
# Final formatted output screen par print karein.

name = input("Enter your Name: ")
phone_num = input("Enter your phone_number:")

first_three_letter = name[0:4]
four_digits =phone_num[-4:]
username = first_three_letter + four_digits
masked_phone = "******" + phone_num[-4:]


print(len(name))
print("Your Username: ", username)
print("Your Masked_phone number: ", masked_phone)


#Project#04: Smart Password Health & Hint Generator
# (Mini Security & String Analyzer)

# Scenario: Jab aap koi password set karte hain, toh system dekhta hai ki password ki length 
# kitni hai aur user ko aage-peeche ke characters ka "Hint" generate karke deta hai.

# Requirements:
# User se unka Password input lo.

# Length Check (len()): Password ki total length find karein.

# First & Last Character Extraction (Positive & Negative Indexing): Password ka pehla character aur aakhri
#  character extract karein (Aakhri character ke liye negative indexing -1 use karein).

# Middle Secret String (Slicing): Password ke beech ka hissa (first aur last character ko chhod kar) extract karein.

# Security Hint (Concatenation): First character + middle hidden string + last character se ek secure hint banayein.

password= input("Enter password:")
length = len(password)
first_char = password[0]
last_char = password[-1]
middle_secret = password[1:-1]

star = "*"*(length-2)
security_hint = first_char + star + last_char 

#output Display
print("-------smart password & Hint Generator------")
print("Length of the password:",length)
print("First extract letter: ",first_char)
print("last extract letter: ",last_char)
print("Middle_sceret: ", middle_secret)
print("You can take Hint: ", security_hint)
