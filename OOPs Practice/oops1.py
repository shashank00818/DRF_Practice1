# A simple class with some methods and objects

class complex:

  def __init__(self,real,imag):
    self.real=real
    self.imag=imag

  def print(self):
    print(str(self.real)+"+ i"+str(self.imag))

  def add(self,c):
    self.real=self.real+c.real
    self.imag=self.imag+c.imag

c1 = complex(10,20)
c1.print()
c2 = complex(20,30)
c1.add(c2)
c1.print()