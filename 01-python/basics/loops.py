#def username(name):
#        if len(name) > 3 and len(name) < 15:
#           while True:
#               print("Valid name. Welcome, " + name + "!")
#               break
#        else:
#            print("Invalid name. Name must be between 3 and 15 characters long.")
#username("John Doe")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  #print(thislist[i])
  thislist = ["apple", "banana", "cherry"]
for x in thislist:
  #print(x)

thislist = ["a", "b", "c", "d", "e"]
i = 0
while i < len(thislist):
  #print(thislist[i])
  i = i + 1
mylist = ["amna", "ali", "ahmed", "hassan"]
notmylist = []
for x in mylist:
  if "a" in x:
    notmylist.append(x)                         
    #print(notmylist)
newlist = [x for x in mylist if "h" in x]
#print(newlist)
forsort = [14, 5, 2, 8, 1]
forsort.sort(reverse=True)
#print(forsort)
thelist = ["banana", "Orange", "Kiwi", "cherry"]
thelist.reverse()
#thelist.sort(key = str.lower)
#print(thelist)
#To copy
#cclist = thislist.copy()
#cclist = forsort[:]
#cclist = list(thislist)
#print(cclist)   
