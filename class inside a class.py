class Company:
    def __init__(self,name,location,director,manager):
        self.c_name=name
        self.location=location
        self.director=director
        self.manager=manager
    def start(self):
        print("company started")


class Employee(Company):
    
    def __init__(self,name,salary,comp:Company):
        self.name=name
        self.salary=salary
        self.company=comp

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print (f"company:comp:{self.company.c_name}")
        print(f"Location{self.company.location}")
        print(f"Director:{self.company.director}")
        print(f"Manager:{self.company.manager}")
    c_obj=Company("nesto","india","abc","xyx")
    c1_obj=Company("hgf","delhi","jed","ths")
    e1_Employee("arun","10000",c_obj)
    e2_Employee("akhil","50000,c1_obj")

    e1.display()
    e2.display()
    e2.start()


    


