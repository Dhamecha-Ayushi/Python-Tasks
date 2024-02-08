#inheritance

class A:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)
#child class
class B(A):
    def __init__(self, name, age):
        self.age = age
        A.__init__(self, name)
        print(self.age)
    
# obj = A("Ayushi")
# 
obj = B("Ayushi",12)
obj.display()