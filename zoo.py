class Zoo:
    def __init__(self,name,location):
        self.z_name=name
        self.location=location

class Animal(Zoo):
    def __init__(self,a_name,species,age,zoo:Zoo):
        self.a_name=a_name
        self.species=species
        self.age=age
        self.zoo=zoo
    def details(self):
        print("Animal details")

    def display(self):
        print(f"Name:{self.a_name}")
        print(f"Species:{self.species}")
        print(f"Age:{self.age}")
        print(f"{self.zoo.z_name}")
        print(f"{self.zoo.location}")

z_obj=Zoo("Zoo world","kerala")
a_obj=Animal("monkey","adf",2,z_obj)
a_obj.details()
a_obj.display()

