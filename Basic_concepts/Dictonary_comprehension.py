#Key comprehensions

keys = {'a', 'b', 'c', 'd', 'e'}
values = {2, 3, 4, 5, 6}
d1 = {'a': 2, 'b':3, 'c': 4, 'd':5}
#print values with key
dict1 = {k:v for (k,v) in zip(keys, values)}
print(dict1)

#print square upto 5 
dict2 = {x: x**2 for x in range(5)}
print(dict2)

#nested dictionary comprenhion

dict2 = {k:v for (k, v) in d1.items() if v %2 == 0}
print(dict2)