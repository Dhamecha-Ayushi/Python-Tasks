#List Operations

lst1 = [1, 2, 3]
lst2 = ["Red", "Yellow", "Blue"]

print(lst1+lst2) #Concatenation
print(lst1*2) #Repetation
print(3 in lst1) #Membership

#Access list items

print(lst1[2], lst2[-1]) 

#Change List items

lst1[2] = 5
print(lst1)

lst1[:2] = lst2
print(lst1)

#Add List items

print("\nAdd Items:\n")
lst1.append(6)
print(lst1)

lst2.insert(1,"Black")
print(lst2)

#Remove List items

print("\nRemove Items:\n")
lst1.pop(3)
print(lst1)

lst2.remove("Red")
print(lst2)
del lst1[3]
print(lst1)

#Loop Lists

for n in lst1:
    print(n, end=" ")
print("\n")
length = range(len(lst2))
for i in length:
    print("lst[{}]".format(i),lst2[i])

#List Comprehension


chars = [char for char in 'Hello' if char not in 'aeiou']
print(chars)
Sqrt = [x**2 for x in range(2,6)]
print(Sqrt)

print(lst1,"\n\n", lst2,"\n\n")
a = [(x,y) for x in lst1 for y in lst2]
print(a)    #combine list using nested list comprehension

a = [x for x in range(1,11) if x%2==0]
print(a)

#Sort List

lst3 = [2, 5, 8, 1, 0]

lst3.sort()
print("Ascending Order: ", lst3)

lst3.sort(reverse=True)
print("\nDescending Order: ", lst3)

#Copy List

lst4 = lst3
print(lst4)

lst3[3] = 100
print(lst3,"\n", lst4)

lst5 = lst3.copy()  #using copy() method
lst3[4] = 200
print(lst5, "\n", lst3)

#Join List

l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = l1+l2
print("\nJoin List: ", l3)