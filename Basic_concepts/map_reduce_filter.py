from functools import reduce

#map
list1 = ["one", "two", "three","four"]
list2 =[2, 3, 4, 5]

#print all values in uppercase
newlist = list(map(str.upper, list1))
print("Upper Case: ", newlist)

newlist = list(map(lambda x:x**2, list2))
print("Square root: ", newlist)

#filter

newlist = list(filter(lambda x: x<15, newlist))
print("Less than 15: ", newlist)

#reduce

fact = reduce(lambda x, y : x*y, [1, 2, 3, 4, 5])
print("Factorial: ", fact)

max = reduce(lambda x, y: x if x > y else y, list2)
print("Max Number: ", max)
