# Abstract class in python
from abc import ABC ,abstractmethod

class Father(ABC):
  @abstractmethod
  def disp(self):
    pass
  def show(self):
    print("concreate method")

class Child(Father):
  def disp(self):
    print("child class ")
    print("defining abstract method")

c = Child()
c.disp()
c.show()