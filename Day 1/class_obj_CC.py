#Coding Challenge

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display(self):
        print("Car Make: ",self.make, "\nCar Model: ",self.model, "\nCar Year: ", self.year)
      
car1 = Car("BMW", "i4", 2020)
car2 = Car("Mercedes-Benz", "GLA", 2022)
print("--Car1--")
car1.display()
print("\n--Car2--")
car2.display()
