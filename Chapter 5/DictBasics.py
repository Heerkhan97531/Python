#dictonary basics n python
student = {
    "name": "Ayra khan",
    "age": 19,
    "city": "Sialkot",
    "Qualification": "Bs.IT",
    "Semester": 6
}
print(student)
print(student["Qualification"])
student["favsubject"] = "Network security"
print(student)
student.pop("favsubject")
print(student)
student.keys()
print(student)
student.values()
print(student)
student.items()
print(student)
print(type(student))