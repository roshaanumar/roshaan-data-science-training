#Example 1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thatlist = ["cucumber", "tomato", "pepper"]
print(thislist[-3])
print(thislist[3:7])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
if "cherry" in thislist:
    print("Yes, 'cherry' is in the fruits list")
thislist[1:4] = ["blackcurrant", "watermelon"]
thislist.insert(4, "watermelon")
thislist.append("grape")
thislist.extend(thatlist)
print(thislist)
thislist.remove("grape")
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)

#Example 2
multiples = []
for i in range(1, 11):
    multiples.append(i * 7)
print(multiples)

#List comprehension
multiples = [x*7 for x in range(1, 11)]
print(multiples)

#Example 3
languages = ["Python", "Java", "C++", "JavaScript"]
length = [len(language) for language in languages]
print(length)

#Example 4
z = [x for x in range(1, 101) if x % 3 == 0]
print(z)
