# Coding Challenge

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display(self):
        print("Car Make: ",self.make, "\nCar Model: ", self.model, "\nCar Year: ",self.year)

car = Car("Mercedes-Benz", "GLA", "2020")
car.display()