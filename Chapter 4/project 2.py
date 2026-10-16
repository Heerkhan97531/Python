#-------Python Project-----------
print("\n======= Employee Evaluation & Role Assignment System=========\n")

Employee_basicdet = ("Ahmad", 22,"Developer")
print("Employee Details:",Employee_basicdet)
perf_score = [85,89,95,72,36]
print("Original Score:",perf_score)

min_score = min(perf_score)
perf_score.remove(min_score)
print(f"Removes lowest score: ({min_score}): ",perf_score)
perf_score.append(94)
print("Update the list value:", perf_score)

avg_score = sum(perf_score)/len(perf_score)
print("Average performance score:",round(avg_score, 2))
if avg_score>=85:
    print("Promoted to Senior Developer & Eligible for Bonus:")
elif 70<= avg_score<85:
    print("Perrformance is good and perfect Retin current role:")
else :
    print("Need Improvement training")    
