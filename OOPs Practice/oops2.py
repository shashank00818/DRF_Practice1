# CLASS MEMBER ACCESS IN PYTHON

# 1. In python, every member is accessible everywhere

# class test:

#   def __init__(self,x,y):
#     self.x=x
#     self.y=y

#   def fun(self):
#     print("Hi")

# t=test(10,20)
# print(t.x)
# print(t.y)
# t.fun()

# 2. When we use "ONE UNDERSCORE" before a variable name, we suggest not to use it outside class (Still user can access it)

# class test:

#   def __init__(self,x,y):
#     self._x=x
#     self.y=y

#   def _fun(self):
#     print("Hi")

# t=test(10,20)
# print(t._x)
# print(t.y)
# t._fun()

# 3. When we use "TWO UNDERSCORE" the variable become private

class test:

  def __init__(self,x,y):
    self.__x=x
    self.y=y

  def __fun(self):
    print("Hi")

t=test(10,20)
print(t.__x) # NOW it will give error
print(t.y)
t.__fun() # NOW it will give error