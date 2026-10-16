# Problem Statement / Requirements:

# Student ka naam aur marks input() ke zariye lein.

# Percentage calculate karein: (obtained_marks / total_marks) * 100.

# Screen par student ka final record print karein.

# Python ka internal concept dikhane ke liye variable ka memory address id(student_name) print karke dikhasei

print("-----Student Grade &Memory Tracking-----")
student_name = input("Enter the name of the student: ")
total_marks = float(input("The total marks of the student: "))
obtained_marks = float(input("The obtained marks of the student: "))

#calculatoin
marks_percentage= (obtained_marks /total_marks)*100
#result of the student
print("Student: ", student_name)
print("The student obtained marks percentage: ", round(marks_percentage, 2), "%" )
print("memory stoage of variable student_name: ",id(student_name))