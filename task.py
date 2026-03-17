#1)

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

print(".................................................................................................")

#2)

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

print(".................................................................................................")

booklist = [("Rishu","AAAA",2025),("Anjali","BBBB",2024),("Rishu","CCCC",2023),("Rishu","DDDD",2022),("Anjali","EEEE",2022)]
lst = ()
for i in booklist:
 output = {
  "Author":i[0],
  "Book":i[1],
  "Year":i[2]
}
print(output)


        
    
