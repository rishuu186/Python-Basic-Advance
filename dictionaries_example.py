#1) Python Dictionaries(Ordered)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
print(thisdict)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22
}    
print(thisdict["surname"])

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22,
    "age" : 28
}    
print(thisdict)

#Dictionary Length
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22,
    "age" : 28
}    
print(len(thisdict))

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
print(type(thisdict))

#The dict() Constructor
thisdict = dict( name="Rishita",surname="Sainy",age=22)
print(thisdict)
print(".................................")

#2) Python - Access Dictionary Items

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
x = thisdict["surname"]
print(x)

#get()
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
x = thisdict.get("surname")
print(x)

#keys()
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
x = thisdict.keys()
print(x)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
x = thisdict.keys()
print(x)
thisdict["clg"]="Sou"
print(x)

#value()
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
x = thisdict.values()
print(x)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
x = thisdict.values()
print(x)
thisdict["clg"]="Sou"
print(x)

# item()
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
x = thisdict.items()
print(x)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
x = thisdict.items()
print(x)
thisdict["clg"]="Sou"
print(x)

#Check if Key Exists
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
if "age" in thisdict:
    print("Yes")
print(".................................")

#3) Python - Change Dictionary Items

#Change Dictionary Items
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
thisdict["age"]=23
print(thisdict)

#Update Dictionarytg
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
thisdict.update({"age":23})
print(thisdict)
print(".................................")

#4) Python - Add Dictionary Items

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
thisdict["clg"]="Sou"
print(thisdict)

#Update Dictionary
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
thisdict.update({"clg":"Sou"})
print(thisdict)
print(".................................")

#5) Python - Remove Dictionary Items

#pop()
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
thisdict.pop("age")
print(thisdict)

#popitem()
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
thisdict.popitem()
print(thisdict)

#del
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
del thisdict["surname"]
print(thisdict)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
del thisdict
#print(thisdict)

#clear()
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
thisdict.clear()
print(thisdict)
print(".................................")

#6) Python - Loop Dictionaries

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
for x in thisdict:
    print(x)
    

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
for x in thisdict:
    print(thisdict[x])

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
for x in thisdict.keys():
  print(x)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
for x in thisdict.values():
  print(x)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
for x,y in thisdict.items():
  print(x,y)
print(".................................")

#7)Python - Copy Dictionaries

#copy()
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
newdict = thisdict.copy()
print(newdict)

#dict()
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
newdict = dict(thisdict)
print(newdict)
print(".................................")

#8) Python - Nested Dictionaries

studentlist = {
   "1": {
      "name":"Abc",
      "year":"20"
   },
   "2":{
      "name":"Dfg",
      "year":"21"
   },
   "3":{
      "name":"Rsgf",
      "year":"23"
   }
}
print(studentlist)

#add three dictionaries into a new dictionary
student1 = {
   "name":"Abc",
   "year":"20"
}
student2 = {
   "name":"Dfg",
   "year":"21"
}
student3 = {
   "name":"Rsgf",
   "year":"23"
}
Stdname = {
   "en1": student1,
   "en2": student2,
   "en3": student3,
}
print(Stdname)

#Nested Dictionaries
studentlist = {
   "1": {
      "name":"Abc",
      "year":"20"
   },
   "2":{
      "name":"Dfg",
      "year":"21"
   },
   "3":{
      "name":"Rsgf",
      "year":"23"
   }
}
print(studentlist["1"]["name"])

#Loop Through Nested Dictionaries
studentlist = {
   "1": {
      "name":"Abc",
      "year":"20"
   },
   "2":{
      "name":"Dfg",
      "year":"21"
   },
   "3":{
      "name":"Rsgf",
      "year":"23"
   }
}
# for x , r in studentlist.items():
#    print(x)

#    for y in r:
#        print(y = ":", r[y])

for x, R in studentlist.items():
    print(x)
    
    for y in R:
        print(y + ':', R[y])
print(".................................")

#9)Python Dictionary Methods

#clear() Method
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
thisdict.clear()
print(thisdict)

#copy() Method
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
r = thisdict.copy()
print(r)

#fromkeys() Method
x = ("1","2","3")
y = "en"
thisdict = dict.fromkeys(x,y)
print(thisdict)

#get() Method
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
r = thisdict.get("surname")
print(r)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
r = thisdict.get("year",2005)
print(r)

#items() Method
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
r = thisdict.items()
print(r)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
r = thisdict.items()
thisdict["clg"]="Sou"
print(r)

#keys() Method
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
r = thisdict.keys()
print(r)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
r = thisdict.keys()
thisdict["clg"]="Sou"
print(r)

#pop() Method
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
thisdict.pop("age")
print(thisdict)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
r = thisdict.pop("age")
print(r)

#popitem() Method
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
thisdict.popitem()
print(thisdict)

thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
r = thisdict.popitem()
print(r)

#setdefault() Method
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
r = thisdict.setdefault("age","20")
print(r)

#update() Method
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
thisdict.update({"clg":"Sou"})
print(thisdict)

#values() Method
thisdict = {
    "name":"Rishita",
    "surname" : "Sainy",
    "age" : 22 
}
r = thisdict.values()
print(r)

studentinfo = {
  "Name":"Rishita",
  "Surname":"Sainy",
  "DOB":"18/6/2005",
  "Age":21
}
print(studentinfo)
print(studentinfo["Age"])
print(studentinfo.keys())
print(studentinfo.values())
print(studentinfo.items())
print(studentinfo.get("Name"))
