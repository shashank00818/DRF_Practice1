# Inheritance

# class Person:
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name

# class Employee(Person):   
#     def __init__(self,id,name,salary):
#         super().__init__(id,name)
#         self.salary=salary

#     def printdetails(self):
#         print(self.id)
#         print(self.name)
#         print(self.salary)

# e=Employee(101,"Rahul",4000)
# e.printdetails()

# Multilevel Inheritance

class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def printdetails(self):
        print(self.id)
        print(self.name)

class Employee(Person):   
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary=salary

    def printdetails(self):
        super().printdetails()
        print(self.salary)


class SalesEmployee(Employee):   
    def __init__(self,id,name,salary,si):
        super().__init__(id,name,salary)
        self.salInc=si

    def printdetails(self):
        super().printdetails()
        print(self.salInc)

se=SalesEmployee(101,"Rahul",4000,2000)
se.printdetails()
e=Employee(102,"Ram",5000)
print()
e.printdetails()