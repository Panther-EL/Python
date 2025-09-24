#Student Report System
class Student:
    def __init__(self, name:str, age:float, grade:str):
        #Assign to self object
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_details(self):
        return f'Name:{self.name},Age:{self.age} years old,Grade:{self.grade}'
    
#Main Program
student = Student('Ivy',14,'A') #Object creation
student_1 = Student('James',15,'B')
student_2 = Student('Lisa',16,'A')
student_3 = Student('Kelvin',14,'A')
student_4 = Student('Janice',19,'C')

print(student.get_details()) #Displaying student details
print(student_1.get_details())
print(student_2.get_details())
print(student_3.get_details())
print(student_4.get_details())
   
