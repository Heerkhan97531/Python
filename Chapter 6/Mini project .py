# pyhton project
print("=========Employee Salary & Attendance Analyzer========")

names = ["Ali", " Ahmad", " Huraira", "Ayra", " Laiba"]
working_hours = [140, 165, 142, 149 , 0]

for emp_id , (name, hour) in enumerate(zip(names, working_hours), start = 1):
    print(f"Employee_ID ={emp_id} | Name = {name} | working hours = {hour}")

attendance = [hours >=160 for hours in working_hours]  
print("\nfull time employee", attendance)

for name in names:
    if name.strip()=="Ali":
        print("\n Yes, it consist targets name.")
        break
else:
    print("Opps!, Targeted employee can't be findout.")

print("---------------End----------------------")    