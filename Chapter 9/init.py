

class student:
    schoolname= "Becone house school system"

    def __init__(self,schoolname, course):
        self. schoolname= schoolname
        self.course= course
        # print(self.schoolname) # you can use this method or not it's up to you
        # print(self.course)
        # print("show the function of init whenever t called or not")

student1= student("Becone House School System","BSIT")
# print(student1) # this is for to see the space that is allocate to the object whenever it created
print(student1.schoolname) # this show the value of attribute
print(student1.course)

student2= student("PGC","BSCS")
print(student2.schoolname) # this show the value of attribute
print(student2.course)
# print("the value of student 2 will be changed and init functon will provide it the different value:  ", student2)
