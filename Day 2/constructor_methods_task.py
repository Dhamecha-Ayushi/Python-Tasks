#Constructors and Methods

#Implement a simple constructor

#Non-parameterized
class Myclass:
    
    def __init__(self):
        self.a = 10
        self.b = 20
obj = Myclass()
print("A = ", obj.a, "\nB = ", obj.b)

#Parameterized
class add:
    'Parameterized Constructor' #documentation
    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2
        self.ans = self.a + self.b
val = add(10, 20)
print("Addition of {} and {} : {}".format(val.a, val.b, val.ans))

#Constructor built-in class function
print("\nConstructor built-in class function:\n")
print("\"getattr\": ",getattr(val, 'a'))
setattr(val, 'a', 20)
print("\"setattr\": ",getattr(val, 'a'))
delattr(val, 'a')
print("\"hasattr a\": ",hasattr(val, 'a'))
print("\"hasattr b\": ",hasattr(val, 'b'))

#Constructor built-in class attributes
print("\nConstructor built-in class attributes:\n")
print("\".__doc__\": ",val.__doc__)
print("\".__dict__ \": ",val.__dict__)
print("\".__module__\": ",val.__module__)
print("\".__name__ \": ",add.__name__)
print("\".__bases__ \": ",add.__bases__)
