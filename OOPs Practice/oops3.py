# Class Method

# class Employee:
#     compName="gfg"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     @classmethod
#     def setcompname(cls,cName):
#         cls.compName=cName

# Employee.setcompname("geeksforgeeks")
# print(Employee.compName)
# e=Employee("Sandeep",41)
# print(e.compName)

# Static method

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @staticmethod
    def isAdult(age):
        return (age>18)
    
    def printdetails(self):
        print(self.name)
        print(self.age)

p=Person("Nikhil",22)
p.printdetails()
print(Person.isAdult(24))
