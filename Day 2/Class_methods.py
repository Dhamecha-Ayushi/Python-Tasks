# Instance, class, static methods, Accessor, Mutator

#instance Method
class method:
    def instance(self):
        return "Instance method is called", self
    #Class Method
    @classmethod
    def class_method(cls):
        return "Class method is called", cls
    def Class_Method(cls):
        return "Second way to define Class Method", cls
    
    #Static Method
    @staticmethod
    def static_method():
        return "Satic method is called"
obj = method()
print(method.instance(obj))
print(method.class_method())
method.Class_Method = classmethod(method.Class_Method)
print(method.Class_Method())
print(method.static_method())

class acc_mut:

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
a = acc_mut()
a.setName("Ayushi")
print(a.getName())