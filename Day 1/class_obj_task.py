#Classes and objects

class Person: #define a class name Person with two attributes Name and Age

    a = 10 #class attribute
    def __init__(self, name, age): 

        self.a = 20
        self.name = name #instance attribute
        self.age = age

p = Person("Ayushi", 22) #instantiate an object name p and pass 2 arguments to the constructor method

print("Name: ",p.name)
print("Age: ", p.age)

print(p.a) #access via instance of the class
print(Person.a) #access via class name