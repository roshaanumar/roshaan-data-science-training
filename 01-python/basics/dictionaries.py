thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
y = thisdict.get("brand")
print(x)
print(y)
z = thisdict.keys()
print(z)
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
car["color"] = "white"
#after the change
a = thisdict.values()
print(a)
for k in thisdict:
  print(k)
for v in thisdict:
  print(thisdict[v])