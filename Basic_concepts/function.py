#Arithmatic Operator
#add
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
def addop(n1, n2):
    return n1 + n2
print("Addition: ",addop(num1, num2))

#sub
def subop(n1, n2):
    return n1 - n2
print("Subtraction: ", subop(num1,num2))

#Comparison Operator
def leqop(n1, n2):
    return n1 <= n2
print(leqop(num1,num2))