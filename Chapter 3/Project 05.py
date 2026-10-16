#----------------MINI PROJECT-----------------
   #Smart Text and Log Data Cleaning Engine
raw_log = "\n\t USER_ID:#10492 | STATUS: ACTIVE | E_mail: LAIBA.DEV@DOMAIN.COM | " \
"ROLE: python developer\n"

log = raw_log.removeprefix("\n").removeprefix("\t").replace(" ","").lstrip()
print(log)

user_raw_log = "USER_ID:#10492"
user_id = user_raw_log.split("#")[1]

Email_address_raw = "LAIBA.DEV@DOMAIN.COM"
Email_Address = Email_address_raw.lstrip().lower()

role_raw = "python developer"
role = role_raw.replace(" ","_").title()

has_at = "@" in Email_Address
has_com = ".com" in Email_Address

search = raw_log.find("active")
search_1 = raw_log.count("active")
print(search)
print(search_1)
length = len(raw_log)
print(length)

#output Display
print("==========================================")
print("          Data Cleaning Report            ")
print("==========================================")
print(f"User_id       : {user_id}")
print(f"Email_Address :{Email_Address}")
print(f"User_role      : {role}")
print(f"Account Status : Active")
print("--------------------------------------------")
print(f"Validaton      : Email Validation{has_at and {has_com}}")
print(f"Total Length of raw input: {length}")
print(f"===========================================")
