# #1) list = input("mummy su su lavu che?")
# # Shooping_list = list.split(",")
# # print(Shooping_list)
# # #sugar, tea, milk ,rice ,garam mashala ,butter Milk 

# # Mummy = input("List barabar che ?")
# # if Mummy == "ha":
# #     print("ok")
# # elif Mummy == "na":
# #     a = input("you want to add or remove something?")
# #     print(a)
# #     if a == "add":
# #         b = input("what?")
# #         Shooping_list.append(b)
# #         print(Shooping_list) 
# #     elif a == "remove":
# #         x = input("what?")
# #         Shooping_list.remove(x)
# #         print(Shooping_list)
# #     else:
# #         print("wrong input")


# # Mummy2 = input("List barabar che ?")
# # if Mummy2 == "ha":
# #     x = input("pakkuu?")
# #     print(x)
# #     if x == "ha":
# #         print("saru")
# #     elif x == "na":
# #         print("to?")
# #         a = input("kay biju lavu che?")
# #         if a == "ha":
# #           b = input("su?")
# #           Shooping_list.append(b)
# #           print(Shooping_list) 
# #           a = input("Su kasu lavanu nathi?")
# #         elif a == "ha":
# #          x = input("su?")
# #          Shooping_list.remove(x)
# #          print(Shooping_list)
# #         else:
# #          print("wrong input")
# # else:
# #    print("ok Mummy")

# # Mummy3 = input("List barabar che ?")
# # if Mummy3 == "ha":
# #     x = input("sure?")
# #     print(x)
# #     if x == "ha":
# #         print("saru")
# #     elif x == "na":
# #         print("to?")
# #         a = input("kay biju lavu che?")
# #         if a == "ha":
# #           b = input("su?")
# #           Shooping_list.append(b)
# #           print(Shooping_list) 
# #           a = input("Su kasu lavanu nathi?")
# #         elif a == "ha":
# #          x = input("su?")
# #          Shooping_list.remove(x)
# #          print(Shooping_list)
# #         else:
# #          print("wrong input")
# # else:
# #    print("ok Mummy")


# #2)
# asking_mom = input("mummy su su lavu che?")
# Shooping_list = asking_mom.split(",")
# print(Shooping_list)
# asking_mom = "na"
# #sugar, tea, milk ,rice ,garam mashala ,butter Milk 

# asking_mom = input("List barabar che ?")   
# if asking_mom == "ha":
#     print("ok")
# elif asking_mom == "na":
#     while asking_mom == "na":
#         asking = input("you want to add or remove something?")
#         print(asking)
#         if asking == "add":
#             add_item = input("what?")
#             Shooping_list.append(add_item)
#             print(Shooping_list) 
#         elif asking == "remove":
#             remove_item = input("what?")
#             Shooping_list.remove(remove_item)
#             print(Shooping_list)
#         else:
#             print("wrong input")
#         asking_mom = input("List barabar che ?")  
#         if asking_mom == "ha":
#             print("hiiii,okayy")

#3) 

tasklist = {
    "task1":"panding",
    "task2":"Done",
    "task3":"Done",
}
for i in tasklist:
    #print(i)
    if tasklist[i] == "Done":
     print(f"{i} pati gyo che mare")
    elif tasklist[i] =="panding":
     print(f"{i} karvano bike che")
    
print(".....................................................................................................")

#4)

num = {1,2,3,4,5,6,7}
out = {
   'odd':[],
   'even':[]
}
for i in num:
    # print(i)
    if i % 2 == 0:
       out["even"].append(i)
    else:
       out["odd"].append(i)
print(out)

print(".....................................................................................................")

#5)

num = [1,2,1,2,3,4,1,4,2]
x = num.count(1)
y = num.count(2)
z = num.count(3)
w = num.count(4)
output = {
    "1":[x],
    "2":[y],
    "3":[z],
    "4":[w]
}
print(output)

num = [1,2,1,2,3,4,1,4,2,97,97,39,46]
output = {}
for i in num: 
    if i in output:
       output[i] += 1
    else:
       output[i] = 1
print(output)

lst = [000,11,22,000,11,22,33,44,55,000,22,33,11,44,55,66]
output = {}
for i in lst:
  if i in output:
    output[i] += 1
  else:
    output[i] = 1
print(output)

print("......................................................................................................................")

#6)

lst=["rishu","rishita","rishu","rishu","rishita"]
x = lst.count("rishu")
y = lst.count("rishita")
output ={
    "rishu":[x],
    "rishita":[y]
}
print(output)

lst=["rishu","rishita","rishu","rishu","rishita"]
output = {}
for i in lst:
    if i in output:
      output[i] += 1
    else:
      output[i] = 1
print(output) 

print(".......................................................................................................................")

#7)

lst = [1,1,1,1,1]
count = 0
for i in lst:
    count += 1
print(count)

print("......................................................................................................................")

#8)

studentinfo = [("Rishita",1516,"BCA",4),("Rishu",1157,"MCA",8),("Dev",462,"BCOM",6)]
for i in studentinfo:
  output = {
        "Name":i[0],
        "IndexNo":i[1],
        "Cource":i[2],
        "Sem":i[3]
      }
  print(output)

print("....................................................................................................................")

studentinfo = [("Rishita",1516,"BCA",4),("Rishu",1157,"MCA",8),("Dev",462,"BCOM",6)]
final = []
for i in studentinfo:
  output = {
"data" : {"Name":i[0],"IndexNo":i[1],"Cource":i[2],"Sem":i[3]}
  }
  final.append(output)
print(final)

print("....................................................................................................................")

#9)

num = [2,6,5,8,5,8,5,9,9,5,2,4,6,8,2,4,2,5,7,2]
output = {
  "odd" : [],
  "oddavg" : 0,
  "even" : [],
  "evenavg" : 0,
  "count" : {},
  "totalavg" : 0
}
for i in num:
  if i % 2 == 0:
    output["even"].append(i)
    output["evenavg"] += i
  else:
    output["odd"].append(i)
    output["oddavg"] += i
  if i in output["count"]:
    output["count"][i] += 1
  else:
    output["count"][i] = 1

output["totalavg"] = sum(num) / len(num)
output["oddavg"] =  output["oddavg"] / len(output["odd"])
output["evenavg"] =  output["evenavg"] / len(output["even"])
print(output)

print("....................................................................................................................")

#10)
studentlist = [{
  "NAME":"Rishita",
  "ROLLNO":1516,
  "SUBJECT":"BCA"
  },
{
 "NAME":"Anjali",
  "ROLLNO":1517,
  "SUBJECT":"MCA"
  },
{
  "NAME":"Heli",
  "ROLLNO":1518,
  "SUBJECT":"BCA"
  }]
output = {}
for i in studentlist:
 print(i)
 if i["SUBJECT"] in output:
   output[i["SUBJECT"]].append(i["NAME"])
 else:
   output[i["SUBJECT"]] = [i["NAME"]]
print(output)

print(".........................................................................................................................")

#11)

dct = {
  "Student": ["Heli","Krishna"],
  "Teacher": ["DhruvSir"],
  "Skills" : ["Python","PHP","AI"]
}
output = {
  "Student":len(dct["Student"]),
  "Teacher":len(dct["Teacher"]),
  "Skills":len(dct["Skills"])
}
print(output)

print("....................................................................................................................")

#12)
booklist = [{
  "Book":"AAAA",
  "Author":"Rishu",
  "Year": 2025
},
{
  "Book":"BBBB",
  "Author":"Anjali",
  "Year": 2025
},
{
  "Book":"CCCCC",
  "Author":"Rishu",
  "Year": 2025
}]
output = {}
for i in booklist:
 print(i)
 if i["Author"] in output:
    output[i["Author"]].append(i["Book"]) 
 else:
    output[i["Author"]] = [i["Book"]]
print(output)

print("......................................................................................")