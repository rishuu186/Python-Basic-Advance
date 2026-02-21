# 1) Strings

print("iTbase")  
print('iTbase')

print("My Name is 'John' ")
print('My Name is "ABC" ')

a = "Python"
print(a)

a = """ Python is a Popular Programing Language, 
Python is high-level Programing Language,
it is easy to use and widely used for many types."""
print(a)
A = '''Python is a Popular Programing Language, 
Python is high-level Programing Language,
it is easy to use and widely used for many types.'''
print(A)
b = """Python is a popular programming language. 
It was created by Guido van Rossum, and released in 1991."""
print(b)
B = """"Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files."""
print(B)

a = "iTbase"
print(a[3])

a = "Python"
print(a[1])

a = "Programing Language"
print(a[9])

a = "Python is a Popular Programing Language"
print(a[20])

for v in "PYTHON":
 print(v)

for a in "ITBASE":
 print(a)

for b in "Popular":
 print(b)

for c in "Programing":
 print(c)

for d in "Language":
 print(d)

a = "ITBASE"
print(len(a))

a = "Python"
print(len(a))

a = "Popular"
print(len(a))

a = "Programing"
print(len(a))

a = "Language"
print(len(a))

txt = "Python is a Popular Programing Language"
print("Python" in txt)

txt = "it can be used on a server to create web applications."
print("Python" in txt)

txt = "Python is high-level Programing Language"
print("Python" in txt)

txt = "Python can be used alongside software to create workflows."
print("Python" in txt)

txt = "It was created by Guido van Rossum, and released in 1991."
print("Python" in txt)

txt = "Python is a Popular Programing Language"
if "Python" in txt:
  print("Yes,'Python'is Present")

txt = "Python is a Popular Programing Language"
print("iTbase" not in txt)

txt = "It was created by Guido van Rossum, and released in 1991."
print("Python" not in txt)

txt = "Python is high-level Programing Language"
print("Programing" not in txt)

txt = "it can be used on a server to create web applications."
print("Python" not in txt)

txt = "Python is a Popular Programing Language"
print("Programing" not in txt)

# 2) Slicing String

a = "Programing Language"
print(a[3:5])

a = "Python is a Popular Programing Language"
print(a[10:22])

a = "Programing Language"
print(a[:5])

a = "Programing Language"
print(a[3:])

a = "Programing Language"
print(a[-5:-2])

# 3) Modify Strigns

a = "Python is a Popular Programing Language(upper)"
print(a.upper())

a = "Upper Case"
print(a.upper())

a = "Programing Language"
print(a.upper())

a = "Python can be used on a server to create web applications."
print(a.upper())

a = "iTbase"
print(a.upper())

a = "Python is a Popular Programing Language(lower)"
print(a.lower())

a = "Lower Case"
print(a.lower())

a = "Programing Language"
print(a.lower())

a = "Python can be used on a server to create web applications."
print(a.lower())

a = "iTbase"
print(a.lower())

a = "Programing Language(Remove WhiteSpace)"
print(a.strip())

a = "iTbase"
print(a.strip())

a = "Python is a Popular Programing Language"
print(a.strip())

a = "Remove WhiteSpace"
print(a.strip())

a = "My Name is John"
print(a.strip())

a = "Python Programing Language"
print (a.replace("P","B"))

a = "My Name is John"
print (a.replace("J","M"))

a = "iTbase"
print (a.replace("T","Y"))

a = "HELLO WORLD"
print (a.replace("L","I"))

a = "Python is a Popular Programing Language"
print (a.replace("i","I"))

a = "Python Programing Language"
print(a.split(" "))

a = "HELLO WORLD"
print(a.split())

a = "iT Base"
print(a.split())

a = "My Name is John"
print(a.split(","))

a = "Py thon"
print(a.split(","))

a = "HELLO,WORLD"
print(a.split(","))

# 4) Concatenation String

a = "Python"
b = "Programing"
c = "Language"
d = a + b + c
print(d)

a = "Python"
b = "Programing"
c = "Language"
d = a + " " + b + " " + c
print(d)

a = "HELLO"
b = "WORLD"
c = a + b 
print(c)

a = "HELLO"
b = "WORLD"
c = a + " " + b 
print(c)

# 5) Format Strings

age = 22
txt = f"My name is John and I am {age} year old"
print(txt)

enum = 23040101516
txt = f"My Enrollment Number is {enum}"
print(txt)

price = 599
txt = f"The Price is {price}"
print(txt)

birthday = 18_06_2005
txt = f"My Birthday Date is {birthday}"
print(txt)

price = 18*2
txt = f"The price is {price}"
print(txt)

# 6) Escape Characters

txt = "Python is a \"Popular\" Programing Language"
print(txt)

txt = "Apple\\Banana\\Cherry"
print(txt)

txt = "Programing\nLanguage"
print(txt)

txt = "Python is a \rPopular Programing Language"
print(txt)

txt = "iT \t Base"
print(txt)

txt = "Programing \bLanguage"
print(txt)

# 7) String Methods

# 1) Capitalize()
  
txt = "python is a Popular Programing Language"
x = txt.capitalize()
print(x)

txt = "iTBase"
x = txt.capitalize()
print(x)

txt = "My Name is John"
x = txt.capitalize()
print(x)

txt = "PYTHON PROGRAMMING"
x = txt.capitalize()
print(x)
 
txt = "capitalize"
x = txt.capitalize()
print(x)

# 2) Casefold()

txt = "python is a Popular Programing Language"
x = txt.casefold()
print(x)

txt = "iTBase"
x = txt.casefold()
print(x)

txt = "My Name is John"
x = txt.casefold()
print(x)

txt = "PYTHON PROGRAMMING"
x = txt.casefold()
print(x)
 
txt = "capitalize"
x = txt.casefold()
print(x)

# 3) Center()

txt = "iTBase"
x = txt.center(20)
print(x)

txt = "My Name is John"
x = txt.center(50,"R")
print(x)

txt = "PYTHON PROGRAMMING"
x = txt.center(20)
print(x)

txt = "HELLO WORLD"
x = txt.center(30,"0")
print(x)

txt = "Dhruv"
x = txt.center(25)
print(x)

# 4) Count()

txt = "I love apples, apples are my Favorite Fruit"
x = txt.count("apple")
print(x)

txt = "I love apples, apples are my Favorite Fruit"
print(txt[10:24])
x = txt.count("apples",10,24)
print(x)

txt = "I love apples, apples are my Favorite Fruit"
print(txt[0:24])
x = txt.count("apples",0,24)
print(x)

txt = "I love mango, apples are my Favorite Fruit"
x = txt.count("mango")
print(x)

txt = "I love mango,mango are my Favorite Fruit"
x = txt.count("mango")
print(x)

# 5) encode
 
txt = "My name is Stålen"
x = txt.encode()
print(x)

txt = "My name is Våle"
x = txt.encode()
print(x)

txt = "My name is Røve"
x = txt.encode()
print(x)

txt = "My name is Våxn"
x = txt.encode()
print(x)

txt = "My name is Råtë"
x = txt.encode()
print(x)

# 6) endwith()

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

txt = "Hello, welcome to my world."
print(txt[5:27])
x = txt.endswith("my world.",5,27)
print(x)

txt = "Hi, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)

txt = "Python Easy"
x = txt.endswith(("Easy","Simple"))
print(x)

# 7) expandtabs()

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

txt = "R\ti\ts\th\ti\tt\ta"
x =  txt.expandtabs(5)
print(x)

txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

txt = "R\ti\ts\th\ti\tt\ta"
print(txt)
print(txt.expandtabs(25))

# 8) Find()

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("world")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("H")
print(x)

txt = "Hello, welcome to my world."
print(txt[5:10])
x = txt.find("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.find("q")) 

# 9) format() Method

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print(txt1)

txt2 = "My name is {0}, I'm {1}".format("John",36)
print(txt2)

txt3 = "My name is {}, I'm {}".format("John",36)
print(txt3)

txt4 = "for only {price}." .format(price=599)
print(txt4)

# 10) format_map() Method
x = {"name" : "John", "age" : 36}
txt = "Happy birthday {name} you are now on level {age}"
print(txt.format_map(x))

# 11) index() Method

a = "Python is a Popular Programing Language(upper)"
print(a.index("Python"))

a = "Upper Case"
print(a.index("e"))

a = "Programing Language"
print(a[0:10])
print(a.index("r",0,10))

a = "Python can  a be used on a server to create web applications."
print(a.index("a"))

a = "iTbase"
#print(a.index("q"))

# 12) isalnum() Method

txt = "Python12"
x = txt.isalnum()
print(x)

txt = "Python 12"
x = txt.isalnum()
print(x)

txt = "Python/12"
x = txt.isalnum()
print(x)

txt = "Pythony@12"
x = txt.isalnum()
print(x)

txt = "Python&12"
x = txt.isalnum()
print(x)

# 13) isalpha() Method

txt = "PythonX"
x = txt.isalpha()
print(x)

txt = "Python10"
x = txt.isalpha()
print(x)

txt = "iTbase"
x = txt.isalpha()
print(x)

txt = "Programing"
x = txt.isalpha()
print(x)

txt = "Language18"
x = txt.isalpha()
print(x)

# 14) isascii() Method

txt = "Python123"
x = txt.isascii()
print(x)

txt = "Python&"
x = txt.isascii()
print(x)

txt = "iTbase"
x = txt.isascii()
print(x)

txt = "Programming"
x = txt.isascii()
print(x)

txt = "P$"
x = txt.isascii()
print(x)

# 15) isdecimal() Method

txt = "51198498646548+845634"
x = txt.isdecimal()
print(x)

txt = "1234"
x = txt.isdecimal()
print(x)

txt = "39656256525284"
x = txt.isdecimal()
print(x)

txt = "C?"
x = txt.isdecimal()
print(x)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

# 16)  isdigit() Method

txt = "22"
x = txt.isdigit()
print(x)

txt = "22/5"
x = txt.isdigit()
print(x)

txt = "22"
x = txt.isdigit()
print(x)

txt = "22@"
x = txt.isdigit()
print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit())
print(b.isdigit())

# 17)  isidentifier() Method

txt = "python"
x = txt.isidentifier()
print(x)

a = "My Folder"
print(a.isidentifier())

b = "itbase002"
print(b.isidentifier())

c = "2python"
print(c.isidentifier())

d = "my_name"
print(d.isidentifier())

# 18) islower() Method

txt = "hello world!"
x = txt.islower()
print(x)


x = "Itbase"
print(x.islower())

x = "python programing"
print(x.islower())

x = "Programong"
print(x.islower())

x = "john"
print(x.islower())

# 19) isnumeric() Method

txt = "565543"
x = txt.isnumeric()
print(x)

txt = "565+644543"
x = txt.isnumeric()
print(x)

txt = "565543@"
x = txt.isnumeric()
print(x)

txt = "565543?"
x = txt.isnumeric()
print(x)

txt = "565ug543"
x = txt.isnumeric()
print(x)

# 20)  isprintable() Method

txt = "Hello Are you?"
x = txt.isprintable()
print(x)

txt = "Hello\nAre you"
x = txt.isprintable()
print(x)

txt = "Python Programming"
x = txt.isprintable()
print(x)

txt = "pytohn\python"
x = txt.isprintable()
print(x)

txt = "pytohn?"
x = txt.isprintable()
print(x)

# 21)  isspace() Method

txt = "   "
x = txt.isspace()
print(x)

txt = "   i   "
x = txt.isspace()
print(x)

# 22) istitle ()

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

txt = "Hello!"
x = txt.istitle()
print(x)

txt = "Python Programming"
x = txt.istitle()
print(x)

txt = "This is/?"
x = txt.istitle()
print(x)

txt = "My World!"
x = txt.istitle()
print(x)

# 23) isupper() Method

txt = "Python Programing"
x = txt.isupper()
print(x)

txt = "PYTOHN"
x = txt.isupper()
print(x)

txt = "Hello World!"
x = txt.isupper()
print(x)

txt = "ITBASE"
x = txt.isupper()
print(x)

txt = "THIS0000"
x = txt.isupper()
print(x)

# 24) join() Method

myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)
print(x)

myTuple = ("ABC", "THNFC", "RGNFD")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

myDict = {"name": "John", "country": "Norway"}
x = "TEST".join(myDict)
print(x)

myDict = {"name": "aBS", "country": "THNC"}
x = "US".join(myDict)
print(x)

# 25) ljust() Method

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

txt = "banana"
x = txt.ljust(20, "O")
print(x)

txt = "AMNGO"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

txt = "mANGO"
x = txt.ljust(20, "O")
print(x)

# 26) lower() Method

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

txt = "pyThon prOgraMing"
x = txt.lower()
print(x)

txt = "itBase"
x = txt.lower()
print(x)

txt = "MY NAME IS JOHN"
x = txt.lower()
print(x)

txt = "PYTHON PROGRAMING"
x = txt.lower()
print(x)

# 27)  lstrip() Method

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)

# 28) maketrans() Method

txt = "Hello Sam"
mytable= str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "python programing"
mytable= str.maketrans("p", "s")
print(txt.translate(mytable))

txt = "Itbase"
mytable= str.maketrans("S", "e")
print(txt.translate(mytable))

txt = "PPPPPDS$SFSZFZ"
mytable= str.maketrans("P", "7")
print(txt.translate(mytable))

txt = "My Name is John"
mytable= str.maketrans("J", "s")
print(txt.translate(mytable))

# 29) partition() Method

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)

txt = "python is a Popular Programing Language"
x = txt.partition("Popular")
print(x)

txt = "python is a Popular Programing Language"
x = txt.partition("java")
print(x)

txt = "Python is a Popular Programing Language"
x = txt.partition("python")
print(x)

# 30) replace() Method

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

txt = "I love apples, apples are my Favorite Fruit"
x = txt.replace("apples", "banana")
print(x)

txt = "I love apples, apples are my Favorite Fruit"
x = txt.replace("apples", "banana", 1 )
print(x)

# 31) rfind() Method

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10)
print(x)

txt = "rishita"
print(txt.rfind("q"))

txt = "Rishit/a"
print(txt.rfind("a"))

# 32) rindex() Method

a = "Python is a Popular Programing Language"
print(a.rindex("Python"))

a = "Upper Case"
print(a.rindex("e"))

a = "Programing Language"
print(a[0:10])
print(a.rindex("r",0,10))

a = "Python can a be used on a server to create web applications."
print(a.rindex("a"))

# a = "iTbase" (error)
# print(a.rindex("q"))

# # 33) rjust() Method

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

txt = "banana"
x = txt.rjust(20, "O")
print(x)

txt = "AMNGO"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

txt = "mANGO"
x = txt.rjust(20, "O")
print(x)

txt = "iTbase"
x = txt.rjust(20, "O")
print(x)

# 34) rpartition() Method

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)

txt = "python is a Popular Programing Language"
x = txt.rpartition("Popular")
print(x)

txt = "python is a Popular Programing Language"
x = txt.rpartition("java")
print(x)

txt = "Python is a Popular Programing Language"
x = txt.rpartition("Python")
print(x)

# 35) rsplit() Method

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

txt = "apple, banana, cherry"
x = txt.rsplit(", ", 1)
print(x)

txt = "aaaaa,bbbbbb,ccccc"
x = txt.rsplit(", ")
print(x)

txt = "aaaaa, bbbbbb, ccccc"
x = txt.rsplit(", ", 1)
print(x)

txt = "python, programing, language"
x = txt.rsplit(",",1)
print(x)

# 36) rstrip() Method

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "banana,,,,,ssqqqww....."
y = txt.rstrip(",.qsw")
print(y)

# 37) split() Method

txt = "Python,Programing,Language"
x = txt.split(",")
print(x)

txt = "welcome to the World"
x = txt.split()
print(x)

txt = "hello, my name is john, I am 26 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#", 1)
print(x)

# 38) splitlines() Method

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(x)

txt = "Python is a Popular Programing Language,\nPython is high-level Programing Language"
x = txt.splitlines()
print(x)

txt = "Python is a Popular \nPrograming \nLanguage"
x = txt.splitlines()
print(x)
 
# 39) startswith() Method

txt ="Python is a Popular Programing Language"
x = txt.startswith("Python")
print(x)

txt = "web development (server-side)"
x = txt.startswith("dev",4,20)
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)

txt = "Hi,welcome to my world."
x = txt.startswith(("Hello","Hi"))
print(x)


# 40) strip() Method

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")


txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)

# 41) swapcase() Method

txt = "Python can be used on a SERVER to create web applications."
x = txt.swapcase()
print(x)

txt = "iTbase"
x = txt.swapcase()
print(x)

txt = "Programing LANGUAGE"
x = txt.swapcase()
print(x)

txt = "Python can be USED on a server TO create WEB applications."
x = txt.swapcase()
print(x)

txt = "Hello My Name Is JOHN"
x = txt.swapcase()
print(x)

# 42) title() Method

txt = "Python Programing"
x = txt.title()
print(x)

txt = "Itbase"
x = txt.title()
print(x)

txt = "MY NAME IS 4687634"
x = txt.title()
print(x)

txt = "PYTOHN"
x = txt.title()
print(x)

txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()

# 43) translate() Method

txt = "Hello Sam"
x = str.maketrans("S", "P")
print(txt.translate(x))

txt = "Python Programing"
x = str.maketrans("P", "R")
print(txt.translate(x))

txt = "ItBAse"
x = str.maketrans("I", "q")
print(txt.translate(x))

txt = "Hello Sam!"
x = str.maketrans("i", "Q")
print(txt.translate(x))

txt = "MY NAME IS JOHN"
x = str.maketrans("J", "S")
print(txt.translate(x))

# 44) upper() Method

txt = "Python is a Popular Programing Language"
x = txt.upper()
print(x)

txt = "iTbase"
x = txt.upper()
print(x)

txt = "My Name is John"
x = txt.upper()
print(x)

txt = "Programing Language"
x = txt.upper()
print(x)

txt = "ython can be used on a server to create web applications."
x = txt.upper()
print(x)

# 45) zfill() Method

txt = "50"
x = txt.zfill(10)
print(x)

txt = "HELLO"
x = txt.zfill(25)
print(x)

txt = "Python Programing"
x = txt.zfill(10)
print(x)

txt = "23010230645964"
x = txt.zfill(100)
print(x)

txt = "Itbase"
x = txt.zfill(29)
print(x)

txt = """Manufacturing industries are central to employment, productivity, exports, and strategic resilience. They warrant a mission-oriented approach beyond incentive-based interventions, the Economic Survey 2025-2026 observed.In the midst of economic transformation, geopolitical uncertainty, and rapid technological change, manufacturing capacity needs to be viewed as a strategic national asset. And, MSMEs are crucial as they should evolve from micro-scale production to deeper participation in formal and export-linked supply chains.The next phase of industrialisation will require a calibrated shift from a model centred mainly on import substitution towards one focused on scale, competitiveness, innovation and deeper integration into GVCs.it noted."""
x = len(txt)
print(txt[0:100])
print(txt[679:749])

txt = """Manufacturing industries are central to employment, productivity, exports, and strategic resilience. They warrant a mission-oriented approach beyond incentive-based interventions, the Economic Survey 2025-2026 observed.In the midst of economic transformation, geopolitical uncertainty, and rapid technological change, manufacturing capacity needs to be viewed as a strategic national asset."""
x = txt.replace(" ","")
print(x)

txt = "Python is a Popular Programing Language" 
x = txt.replace(" ","")
print(x)

txt = "Python is a Popular Programing Language" 
x = txt.replace(" ","<")
print(x)