#Coding Challenge

class Car:
    a = 2024
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def age_count(self,current_year):
        age=current_year-self.year
        return age
    
    def display(self):
        print("Car Make: ",self.make, "\nCar Model: ",self.model, "\nCar Year: ", self.year)

current_year=2024

cars=[
    Car("Mercedes","G-wagon",2006),
    Car("Mahindra","Scorpio",2022),
    Car("Maruti","Swift",2019),
    Car("Hyundai","i20",2008),
    Car("Tata","Altroz",2021),
]
for car in cars:
    car_age= car.age_count(current_year)
    print({car.make}, {car_age})  

