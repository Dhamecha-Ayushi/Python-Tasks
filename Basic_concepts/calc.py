import module

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print(module.add(num1, num2))
print(module.sub(num1, num2))
print(module.mul(num1, num2))
print(module.div(num1, num2))

print(dir(module))