#Coding Challenge 2

class Calculator():

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a+self.b
    def substraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        if self.b != 0:
            return self.a/self.b
        else:
            return "Can't divide by zero"
    def display(self):
        print(self.addition, self.substraction, self.multiplication, self.division)

x = int(input("Enter a: "))
y = int(input("Enter b: "))
obj = Calculator(x, y)
choice = 1
while choice !=0:
   
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nAddition: ", obj.addition())
    elif choice == 2:
        print("\nSubstraction: ", obj.substraction())
    elif choice == 3:
        print("\nMultiplication: ", obj.multiplication())
    elif choice ==4:
        print("\nDivision: ", obj.division())
    elif choice == 5:
        print("Exit")
        break
    else:
        print("\nInvalid Choice!!")