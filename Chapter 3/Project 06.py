#----------------MINI PROJECT-----------------
#Smart Text and Log Data Cleaning Engine

raw_log = "\n \t USER_ID:#10492 | STATUS: active | E_mail:   LAIBA.DEV@DOMAIN.COM | ROLE: python developer "

log= raw_log.removeprefix("\n").removeprefix("\t").replace(" ","").lstrip()
print(log)
user_id_raw = "USER_ID: #10492"
user_id =user_id_raw.split("#")[1]

Email_address_raw = "  LAIBA.DEV@DOMAIN.COM"
Email_address = Email_address_raw.lstrip().lower()

role_raw = "python developer"
role = role_raw.replace(" ", "_").title()

has_at = "@" in Email_address
has_com = ".com" in Email_address

search =  raw_log.find("active")
search_1 = raw_log.count("active")
print(search_1)
print(search)
length = len(raw_log)
print(length)

#output

print("\n================================================")
print("               DATA CLEANING REPORT               ")
print("==================================================")
print(f"User_id       :{user_id}")
print(f"Email Address :{Email_address}")
print(f"User Role     :{role}")
print(f"Account Status:Active")
print("--------------------------------------------------")
print(f"Validation    :Email Validation {has_at and has_com}")
print(f"Total Length of raw input:{length}")
print("==================================================")