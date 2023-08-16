# POLYMORPHISM

class Employee:
    def fun(self):
        print("fun() of Employee")
    
class Customer:
    def fun(self):
        print("fun() of Customer")

l=[Employee(),Customer()]

for x in l:
    x.fun()

# Operator Overloading

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def __add__(self,other):
        return self.price + other.price
    
p1=Product("Keyboard",600)
p2=Product("Mouse",400)
print(p1+p2)