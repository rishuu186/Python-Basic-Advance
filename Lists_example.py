# 1) Python Lists

list1=["apple","banana","mango","cherry",]
print(list1)
list2=[1,2,3,4,5,6,7]
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
print(list5)

#Allow Duplicates
list1=["apple","banana","mango","cherry","banana",]
print(list1)
list4=[1232,1956,2523,4854,5666,2523,5549]
print(list4)

#List Length
list1=["apple","banana","mango","cherry",]
print(len(list1))
list2=[1,2,3,4,5,6,7]
print(len(list2))
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
print(len(list3))
list4=[1232,1956,2523,4854,5666,2523,5549]
print(len(list4))
list5=["suzui","mercedes","honda","jaguar",]
print(len(list5))

#List Items / Data Types
list1=["apple","banana","mango","cherry",]
print(list1)
list2=[1,2,3,4,5,6,7]
print(list2)
list3 = [True, False, False]
print(list3)
list1 = ["abc", 34, True, 40, "male"]
print(list1)

#Data Type()
list1=["apple","banana","mango","cherry",]
print(type(list1))
list2=[1,2,3,4,5,6,7]
print(type(list2))
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
print(type(list3))
list4=[1232,1956,2523,4854,5666,2523,5549]
print(type(list4))
list5=[True, False, False, True, False]
print(type(list5))

#The list() Constructor
list1=(("apple","banana","mango","cherry"))
print(list1)
list2=((1,2,3,4,5,6,7))
print(list2)
list3=(("Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"))
print(list3)
list4=((1232,1956,2523,4854,5666,2523,5549))
print(list4)
list5=(("suzui","mercedes","honda","jaguar",))
print(list5)

# 2) Python - Access List Items

#Access Items
list1=["apple","banana","mango","cherry",]
print(list1[2])
list2=[1,2,3,4,5,6,7]
print(list2[5])
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
print(list3[5])
list4=[1232,1956,2523,4854,5666,2523,5549]
print(list4[2])
list5=["suzui","mercedes","honda","jaguar",]
print(list5[2])


#Negative Indexing
list1=["apple","banana","mango","cherry",]
print(list1[-2])
list2=[1,2,3,4,5,6,7]
print(list2[-5])
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
print(list3[-5])
list4=[1232,1956,2523,4854,5666,2523,5549]
print(list4[-2])
list5=["suzui","mercedes","honda","jaguar",]
print(list5[-2])

#Range of Indexes
list1=["apple","banana","mango","cherry",]
print(list1[2:3])
list2=[1,2,3,4,5,6,7]
print(list2[3:5])
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
print(list3[1:5])
list4=[1232,1956,2523,4854,5666,2523,5549]
print(list4[2:6])
list5=["suzui","mercedes","honda","jaguar",]
print(list5[2:5])

list1=["apple","banana","mango","cherry",]
print(list1[2:])
list2=[1,2,3,4,5,6,7]
print(list2[5:])
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
print(list3[4:])
list4=[1232,1956,2523,4854,5666,2523,5549]
print(list4[3:])
list5=["suzui","mercedes","honda","jaguar",]
print(list5[2:])

list1=["apple","banana","mango","cherry",]
print(list1[:2])
list2=[1,2,3,4,5,6,7]
print(list2[:5])
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
print(list3[:5])
list4=[1232,1956,2523,4854,5666,2523,5549]
print(list4[:2])
list5=["suzui","mercedes","honda","jaguar",]
print(list5[:3])

#Range of Negative Indexes
list1=["apple","banana","mango","cherry",]
print(list1[-4:-2])
list2=[1,2,3,4,5,6,7]
print(list2[-6:-3])
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
print(list3[-7:-1])
list4=[1232,1956,2523,4854,5666,2523,5549]
print(list4[-5:-3])
list5=["suzui","mercedes","honda","jaguar",]
print(list5[-2:-1])

# 3) Python - Change List Items

#Change Item Value
list1=["apple","banana","mango","cherry",]
list1[1]="pineapple"
print(list1)
list2=[1,2,3,4,5,6,7]
list2[5]=8
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3[3]="Anirudh"
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
list4[4]=43215
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
list5[0]="bmw"
print(list5)

#Change a Range of Item Values
list1=["apple","banana","mango","cherry",]
list1[1:3] = ["blackcurrant", "watermelon"]
print(list1)
list2=[1,2,3,4,5,6,7]
list2[2:4]=[2222,33333]
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3[4:5]=["mitul"]
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
list4[3:6]=[3333,4444,5555]
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
list5[1:2]=["BMW"]
print(list5)

# 4) Python - Add List Items

#Append Items
list1=["apple","banana","mango","cherry",]
list1.append("watermelon")
print(list1)
list2=[1,2,3,4,5,6,7]
list2.append(8888)
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3.append("ani")
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
list4.append(698486568)
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
list5.append("BMW")
print(list5)

#Insert Items
list1=["apple","banana","mango","cherry",]
list1.insert(1,"watermelon")
print(list1)
list2=[1,2,3,4,5,6,7]
list2.insert(2,2222)
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3.insert(3,"Ani")
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
list4.insert(4,65989496)
print(list4)
list5=["suzui","mercedes","honda","jaguar"]
list1.insert(4,"bmw")
print(list5)

#Extend List
list1=["apple","banana"]
x=["mango","cherry",]
list1.extend(x)
print(list1)

list2=[1,2,3,4]
x=[5,6,7]
list2.extend(x)
print(list2)

list3=["Hiren","Dev","Sunaj"]
x=["Vibhu","Sahil","Surbhi"]
list3.extend(x)
print(list3)

list4=[1232,1956,2523]
x=[4854,5666,2523,5549]
list4.extend(x)
print(list4)
list5=["suzui","mercedes"]
x=["honda","jaguar"]
list5.extend(x)
print(list5)

#Add Any Iterable
list1=["apple","banana","mango","cherry",]
list2=[1,2,3,4,5,6,7]
list1.extend(list2)
print(list1)

list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list4=[1232,1956,2523,4854,5666,2523,5549]
list3.extend(list4)
print(list3)

# 5) Python - Remove List Items

#Remove Specified Item
list1=["apple","banana","mango","cherry",]
list1.remove("banana")
print(list1)
list2=[1,2,3,4,5,6,7]
list2.remove(4)
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3.remove("Dev")
print(list3)
#remove only first element
list4=[1232,1956,2523,4854,5666,2523,5549]
list4.remove(2523)
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
list5.remove("honda")
print(list5)

#Remove Specified Index
list1=["apple","banana","mango","cherry",]
list1.pop(1)
print(list1)
list2=[1,2,3,4,5,6,7]
list2.pop(5)
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3.pop(3)
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
list4.pop(4)
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
list5.pop(2)
print(list5)

#Remove the last item
list1=["apple","banana","mango","cherry",]
list1.pop()
print(list1)
list2=[1,2,3,4,5,6,7]
list2.pop()
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3.pop()
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
list4.pop()
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
list5.pop()
print(list5)

#del
list1=["apple","banana","mango","cherry",]
del list1[0]
print(list1)
list2=[1,2,3,4,5,6,7]
del list2[1]
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
del list3[2]
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
del list4[5]
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
del list5[3]
print(list5)

#(error)because you deleted "thislist"
# list1=["apple","banana","mango","cherry",]
# del list1
# print(list1)
# list2=[1,2,3,4,5,6,7]
# del list2
# print(list2)
# list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
# del list3
# print(list3)
# list4=[1232,1956,2523,4854,5666,2523,5549]
# del list4
# print(list4)
# list5=["suzui","mercedes","honda","jaguar",]
# del list5
# print(list5)

#Clear the List
list1=["apple","banana","mango","cherry",]
list1.clear()
print(list1)
list2=[1,2,3,4,5,6,7]
list2.clear()
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3.clear()
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
list4.clear()
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
list5.clear()
print(list5)

# 6) Python - Sort Lists

#Sort List Alphanumerically
list1=["apple","banana","mango","cherry",]
list1.sort()
print(list1)
list2=[1,2,3,4,5,6,7]
list2.sort()
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3.sort()
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
list4.sort()
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
list5.sort()
print(list5)

#Sort Descending
list1=["apple","banana","mango","cherry",]
list1.sort(reverse = True)
print(list1)
list1=["apple","banana","mango","cherry",]
list1.sort(reverse = False)
print(list1)
list2=[1,2,3,4,5,6,7]
list2.sort(reverse = True)
print(list2)
list2=[1,2,3,4,5,6,7]
list2.sort(reverse = False)
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3.sort(reverse = True)
print(list3)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3.sort(reverse = False)
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
list4.sort(reverse = True)
print(list4)
list4=[1232,1956,2523,4854,5666,2523,5549]
list4.sort(reverse = False)
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
list5.sort(reverse = True)
print(list5)
list5=["suzui","mercedes","honda","jaguar",]
list5.sort(reverse = False)
print(list5)

#Reverse Order
list1=["apple","banana","mango","cherry",]
list1.reverse()
print(list1)
list2=[1,2,3,4,5,6,7]
list2.reverse()
print(list2)
list3=["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list3.reverse()
print(list3)
list4=[1232,1956,2523,4854,5666,2523,5549]
list4.reverse()
print(list4)
list5=["suzui","mercedes","honda","jaguar",]
list5.reverse()
print(list5)

# 7) Python - Copy Lists

#Copy a List
list1=["copy","apple","banana","mango","cherry",]
mylist = list1.copy()
print(mylist)
list2=["copy",1,2,3,4,5,6,7]
mylist = list2.copy()
print(mylist)
list3=["copy","Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
mylist = list3.copy()
print(mylist)
list4=["copy",1232,1956,2523,4854,5666,2523,5549]
mylist = list4.copy()
print(mylist)
list5=["copy","suzui","mercedes","honda","jaguar",]
mylist = list5.copy()
print(mylist)

#Use the list() method
x=["list","apple","banana","mango","cherry",]
mylist = list(x)
print(mylist)
x=["list",1,2,3,4,5,6,7]
mylist = list(x)
print(mylist)
x=["list","Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
mylist = list(x)
print(mylist)
x=["list",1232,1956,2523,4854,5666,2523,5549]
mylist = list(x)
print(mylist)
x=["list","suzui","mercedes","honda","jaguar",]
mylist = list(x)
print(mylist)

#Use the slice Operator
list1=[":","apple","banana","mango","cherry",]
mylist = list1[:]
print(mylist)
list2=[":",1,2,3,4,5,6,7]
mylist = list2[:]
print(mylist)
list3=[":","Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
mylist = list3[:]
print(mylist)
list4=[":",1232,1956,2523,4854,5666,2523,5549]
mylist = list4[:]
print(mylist)
list5=[":","suzui","mercedes","honda","jaguar",]
mylist = list5[:]
print(mylist)

# 8) Python - Join Lists

#Join Two Lists
list1 = ["apple","banana","mango","cherry",]
list2 = [1,2,3,4,5,6,7]
list3 = list1 + list2
print(list3)

list1 = ["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list2 = [1232,1956,2523,4854,5666,2523,5549]
list3 = list1 + list2
print(list3)

list1 = ["suzui","mercedes","honda","jaguar",]
list2 = [1,2,3,4,5,6,7]
list3 = list1 + list2
print(list3)

#use the extend()
list1 = [1,2,3,4,5,6,7]
list2 = ["apple","banana","mango","cherry",]
list1.extend(list2)
print(list1)

list1 = [1232,1956,2523,4854,5666,2523,5549]
list2 = ["Hiren","Dev","Sunaj","Vibhu","Sahil","Surbhi"]
list1.extend(list2)
print(list1)

list1 = [1,2,3,4,5,6,7]
list2 = ["suzui","mercedes","honda","jaguar",]
list1.extend(list2)
print(list1)

# 9) Python - List Methods

#count() Method
list1=["apple","banana","mango","cherry","banana"]
x = list1.count("banana")
print(x)
list2=[1,2,3,4,5,6,7,5,8,5,9,6,5]
x = list2.count(5)
print(x)
list3=["Hiren","Dev","Sunaj","Vibhu","dev","Sahil","Surbhi","Dev"]
x = list3.count("Dev")
print(x)
list4=[1232,1956,2523,4854,5666,2523,5549,2523]
x = list4.count(2523)
print(x)
list5=["suzui","mercedes","honda","jaguar",]
x = list5.count("bmw")
print(x)
