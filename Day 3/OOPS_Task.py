#Explore and implement nested classes
class Employee:
    def __init__(self):
        self.name = "Ayushi"
        self.addr = self.address()
        return
    def show(self):
        print("Name: ", self.name)
        self.address().display()
    class address:
        def __init__(self):
            self.city1 = "Ahmedabad"
            self.city2 = "Rajkot"
            return
        def display(self):
            print("City: ",self.city1, self.city2)

e = Employee()
e.show()

#super

# class A():
#     def __init__(self, )