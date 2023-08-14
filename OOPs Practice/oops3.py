# Class Method

class Employee:
    compName="gfg"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @classmethod
    def setcompname(cls,cName):
        cls.compName=cName


Employee.setcompname("geeksforgeeks")
print(Employee.compName)
e=Employee("Sandeep",41)
print(e.compName)