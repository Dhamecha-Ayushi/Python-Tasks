def name(fname, lname):
    print("Hello, ", fname, lname)
name("Ayushi", "Dhamecha")

def add(a, b = 10):
    return a+b
#c = add(20)
#print(c)
print(add(20))

def Name(*args):
    print("Hello, ", args[0], args[1])
Name("Dhamecha", "Ayushi")

def val(x, y, z):
    print(f"X:{x}, Y:{y}, Z:{z}\n")
l = [1, 2, 3]
val(*l)

def Name(**kwargs):
    for m,n in kwargs.items():
        print(f'{m}: {n}')
Name(fname = "ayushi",lname = "dhamecha")

def val(a, b, c):
    print(a, b, c)
x = {'a':10, 'b':20, 'c':30}
val(**x)
