thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
thislist.sort(reverse = True)
mylist = thislist.copy()

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

for x in range(len(thislist)):
  if x == 3:
    print(thislist[x])
    break

for x in range(len(mylist)):
  if x == 3:
    print(mylist[x].upper())
    break    


i = 1
b = "*"
while i < 10:
  print(b)
  b = b + "@"
  i += 1
   