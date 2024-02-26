class Course:
    def __init__(self,c_name,description):
        self.c_name=c_name
        self.description=description
    def start(self):
        print("course started")   

class Student (Course):
    def __init__(self,s_name,crs:Course,age):
        self.s_name=s_name
        self.course=crs
        self.age=age
    def details(self):
        print("student details")  

    def display(self):
        print(f"Name:{self.s_name}")
        print(f"Age:{self.age}")
        print(f"course:{self.course.c_name}")
        print(f"description:{self.course.description}")
c_obj=Course("python","python is an open sourse community language.........")
s_obj=Student("arun",c_obj,20)
c_obj.start()
s_obj.details()
s_obj.display()

