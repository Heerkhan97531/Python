#create a class Student that take 3 marks and have a method average().
class Student:
    math = 95
    urdu= 78
    eng = 67
    def average(self):
         total= self.math+ self.urdu+ self.eng
         return total/3
    print()

marks = Student()
print("the marks of the subject urdu-",marks.urdu)
print("The marks of the subject math- ",marks.math)
print("The marks of the subject eng- ",marks.eng)
print(f"student average-{marks.average():.3f}")


# or you can use this -init- method
# you can use static method that don't use "self"' keyword


class Student():
     def __init__(self, name , list_of_marks):
          self.name= name
          self.list_of_marks= list_of_marks 
     def average(self):
        sum=0
        for eachvalue in self.list_of_marks:
          sum= sum+ eachvalue
        average= sum/3
        print("average of marks - ",average)
student1 = Student("ayra", [98,67,78])  
student1.average()     
        
