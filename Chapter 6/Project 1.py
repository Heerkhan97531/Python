#python project #01

print("\n =======Employee Salary & Attendance Analyzer (Data Processing Automation)=========\n ")

names = ["Ali", "Ahmand ","huaira", "haider"]
working_hours = [140, 165, 142, 149]


for emp_id, (name,hour) in enumerate(zip(names, working_hours), start=1):
    print(f"Employee_ID = {emp_id} | Name = {name} | working hours = {hour} ")

attendance = [hours >= 160 for hours in working_hours]
print("\nfull time employee", attendance)

for name in names:
    if name.strip() == "Ali":
        print("\n yes, it consist targetes name.")
        break
else:
    print("opps!, Targeted employee cannot be findout: ")


print("--------------End-----------------")    

#python project 02
