def demo(a: int, b: int):
    c = a + b
    return c
print(demo(10, 20))

def demo(a: int, b: int) -> int:
    c = a + b
    return c
print(demo(20, 30))

def mark(a: "Physics", b: "Maths" = 20) -> int:
    c = a + b
    return c
print(mark(10))
print(mark.__annotations__)