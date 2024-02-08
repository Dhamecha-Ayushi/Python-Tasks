import array as arr

a = arr.array('i', [1, 2, 3, 4])
print(a)

for i in a:
    print(i)

x = 0
print("Using while loop")
while x<len(a):
    print(a[x])
    x+=1

a = arr.array('i', [10,5,15,4,6,20,9])
b = a.tolist()
b.reverse()
a = arr.array('i')
a.fromlist(b)
print (a)

a = arr.array('i', [10,5,15,4,6,20,9])
for i in range(0, len(a)):
   for j in range(i+1, len(a)):
      if(a[i] > a[j]):
          a[i], a[j] = a[j], a[i]
print (a)