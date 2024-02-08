#list comprehension

list1 =["one", "Two", "Three", "Four", "five", "Six"]
list2 = [2, 3, 4, 5, 6, 9]

newlist = [x for x in list1 ]
print(newlist)
 #print element which has letter "i" in it
newlist = [x for x in list1 if "i" in x]
print(newlist)

#print all list elements except "one"
newlist = [x for x in list1 if x != "one"]
print(newlist)

#print even numbers
newlist = [x for x in list2 if x%2==0]
print(newlist)

newlist = [x for x in range(20) if x%2==0]
print(newlist)

newlist = [x for x in "Hello"]
print(newlist)