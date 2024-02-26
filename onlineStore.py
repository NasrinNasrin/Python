class OnlineStore:
    def __init__(self,name,location):
        self.name=name
        self.location=location

class Product(OnlineStore):
    def __init__(self,p_name,price,quantity_in_stock,onlinestore:OnlineStore):
        self.p_name=p_name
        self.price=price
        self.quantity_in_stock=quantity_in_stock
        self.onlinestore=onlinestore
    
    def details(self):
        print("Product details")

    def display(self):
        print(f"Name:{self.p_name}")
        print(f"Price:{self.price}")
        print(f"Quantity:{self.quantity_in_stock}")
        print(f"{self.onlinestore.name}")
        print(f"Location{self.onlinestore.location}")

o_obj=OnlineStore("Pastel Parrot","calicut")
p_obj=Product("Toys",1000,100,o_obj)
p_obj.details()
p_obj.display()

