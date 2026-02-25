#Python For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

list = [1, 5, 7, 9, 3]
for y in list:
  print(y)

A = [True, False, False, True, False, False]
for x in A:
  print(x)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for y in thislist:
  print(y)

list = [10094, 50294, 66515, 94382, 95123]
for x in list:
  print(x)

#Looping Through a String
for x in "apple":
  print(x)

for x in "123456789":
  print(x)

for x in "python itbase.in":
  print(x)

for x in "24":
  print(x)

for x in "bananananannanananna":
  print(x)

#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
list = [1, 5, 7, 9, 3]
for y in list:
  print(y) 
  if y == 7:
    break
list = [1, 5, 7, 9, 3]
for y in list: 
  if y == 7:
    break
  print(y)

A = [True, False, False, True, False, False] #(.........................................................................................................................................)
for x in A:
  print(x)
  if x == False:
    break
A = [True, False, False, True, False, False] 
for x in A:
  if x == False:
    break
  print(x)
  
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for y in thislist:
  print(y)
  if y == "cherry":
    break
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for y in thislist:
  if y == "cherry":
    break
  print(y)

list = [10094, 50294, 66515, 94382, 95123]
for x in list:
  print(x)
  if x == 66515:
    break
list = [10094, 50294, 66515, 94382, 95123]
for x in list:
  if x == 66515:
    break
  print(x)

#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

list = [1, 5, 7, 9, 3]
for y in list: 
  if y == 7:
    continue
  print(y)

A = [True, False, False, True, False, False] 
for x in A:
  if x == False:
    continue
  print(x)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for y in thislist:
  if y == "cherry":
    continue
  print(y)

list = [10094, 50294, 66515, 94382, 95123]
for x in list:
  if x == 66515:
    continue
  print(x)

#The range() Function
for x in range(6):
  print(x) 
for x in range(1):
  print(x) 
for x in range(20):
  print(x) 
for x in range(2):
  print(x) 
for x in range(50):
  print(x) 

for x in range(2,6):
  print(x) 
for x in range(1,2):
  print(x) 
for x in range(2,3):
  print(x) 
for x in range(0,11):
  print(x) 
for x in range(1,50):
  print(x) 

for x in range(2, 20, 2):
  print(x)
for x in range(6, 30, 3):
  print(x)
for x in range(5, 40, 4):
  print(x)
for x in range(1, 100, 5):
  print(x)
for x in range(5, 120, 6):
  print(x)

#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(20):
  print(x) 
else:
  print("Finally finished!")

for x in range(0,21):
  print(x) 
else:
  print("Finally finished!")

for x in range(1,50):
  print(x) 
else:
  print("Finally finished!")

for x in range(1, 100, 5):
  print(x)
else:
  print("Finally finished!")

for x in range(5, 120, 6):
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

for x in range(20):
   if x == 4: break
   print(x) 
else:
  print("Finally finished!")

for x in range(0,21):
   if x == 6: break
   print(x) 
else:
  print("Finally finished!")

for x in range(1,50):
   if x == 2: break
   print(x) 
else:
  print("Finally finished!")

for x in range(1, 100, 5):
   if x == 5: break
   print(x)
else:
  print("Finally finished!")

for x in range(5, 120, 6):
   if x == 3: break
   print(x)
else:
  print("Finally finished!")

#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

car = ["Ford","Mitsubishi","BMW","VW"]
year = [2005,2006,2002,2001]
for x in car:
  for y in year:
    print(x, y)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list1:
  for y in list2:
    print(x, y)

thislist = ["apple", "banana", "cherry"]
list = [100, 50, 65, 82, 23]
for x in thislist:
  for y in list:
    print(x,y)

a = [1,2,3,4]
b = [11,22,33,44]
for x in a:
  for y in b:
    print(x,y)

#The pass Statement
for x in [0, 1, 2]:
  pass

for x in ["apple", "banana", "cherry"]:
  pass

for x in [True, False, False, True, False, False]:
  pass

list = [1, 5, 7, 9, 3]
for y in list:
  pass

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for y in thislist:
  pass

list = [10094, 50294, 66515, 94382, 95123]
for x in list:
 pass

#for loops example(office)
#1
clg = ["dmbs","cn","rdms","iot"]
for i in clg:
  print(i)

#2
attendence = [1,2,3,4,5]
for i in attendence:
   print(i)

#3
read_book = True
page =  [1,2,3,4,5]
for i in page:
   print(i)

#4
# exercise = True
# pushups = input("how many push ups you can do ?")
# for i in range(10):
#    print(i)

#5
photos = "delete"
for i in range(5):
   print(i)

#6
# Chocolate = True 
# share = input("are you want to share chocolate?")
# for i in range(5):
#    print(i)

#7
birthday_photos = "post"
for i in range(10):
   print(i)

#8
compelete = "yes"
for i in compelete:
   print(i)

#9
printnum = ("1 to 100")
for i in range(101):
   print(i)

#10
essay = ("100 words")
for i in range(101):
   print(i)




