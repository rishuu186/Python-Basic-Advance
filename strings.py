#1) Python Strings

# Strings
print("Hello") 
print('Hello')

#Quotes inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign string to a variable
a = "Hello"
print(a)

#Multiline Strings
a = """This is a multiline string.
It can span multiple lines.
No need for \n manually."""
print(a)
a = '''This is a multiline string.
It can span multiple lines.
No need for \n manually.'''
print(a)

#Strings are Arrays
a = "Hello,World"
print(a[3])

#Looping Through a String
for x in "banana":
 print(x)

#String Length 
a = "Hello World!"
print(len(a))

#Check string
txt = "The best things in life are free!"
print("Free" in txt)

#if statement
txt = "The best things in life are free!"
if "free" in txt:
     print ("yes,'Free' is present")

# Check if Not
txt = "The best things in life are free!"
print("expensive" not in txt)

#if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
 print ("No,'expensive' is not Present")

# 2) Python - Slicing Strings

#Slicing
b = "Hello, World!"
print(b[2:5])

#Slice From the Start
b = "Hello World"
print(b[:5])

#Slice To the End
b = "Hello World"
print(b[2:])

#Negative Indexing
b = "Hello World"
print(b[-5:-2])

# 3) Python Modify Strings

#Upper Case
c = "Upper Case"
print(c.upper())

#Lower Case
c = "Lower Case" 
print(c.lower())

#Remove Whitespace
c = "White Spase "
print(c.strip())

#Replace String
c = "Hello World"
print(c.replace("W","R"))

#Split String
a = "Hello World"
print(a.split(" "))

# 4) Python - String Concatenation

#String Concatenation
a = "Hello"
b = "World"
c = a + b 
print(c)

a = "Hello"
b = "World"
c = a +" " + b 
print(c)

# 5) Python - Format Strings

#String Format
age = 28
txt = "My name is John , I am " + age
print(txt)

#F-Strings
age = 28 
txt = f"My Name is John , I am {age}"
print (txt)

#Placeholders and Modifiers
price = 99
txt = f"The Price is {price} Dollars"
print(txt)

price = 99
txt = f"The Price is {price:.2F}"
print(txt)

txt = f"The Price is {20*59} dollars"
print(txt)

#6)Python - Escape Characters

#Escape Character (error)
# txt = "We are the so-called "Vikings" from the north."
# print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#Single Quote
txt = 'It\'s alright.'
print(txt) 

#Backslash 
txt = "This will insert one \\ (backslash)."
print(txt) 

#New line
txt = "Hello\nWorld"
print(txt) 

#Carriage Return
txt = "Hello\rWorld"
print(txt)

#Tab
txt = "Hello \tWorld"
print(txt)

#Backspace
txt = "Hello \bWorld"
print(txt)

#Form Feed

#OctalValue
txt = "\110\145\154\154\157"
print(txt) 

#Hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

#7)Python - String Methods

# 1) capitalize() Method
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "python is FUN!"
x = txt.capitalize()
print (x)

txt = "36 is my age."
x = txt.capitalize()
print (x)

# 2) casefold() Method
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# 3) center() Method
txt = "banana"
x = txt.center(50)
print(x)

txt = "banana"
x = txt.center(20,"0")
print(x)

# 4) count() Method
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "I love apples, apple are my favorite fruit"
print(txt[7:24])
x = txt.count("apple", 7, 24)
print(x)

# 5) encode() Method
txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "My name is rishitå"
x = txt.encode()
print(x)

# 6) endswith() Method
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

txt = "Hello, welcome to my world."
print(txt[5:27])
x = txt.endswith("my world.", 5,27)
print(x)

txt = "Hi, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)

txt = "Python Easy"
x = txt.endswith(("Easy", "Simple"))
print(x)

# 7) expandtabs() Method
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

txt = "R\ti\ts\th\ti\tt\ta"
x =  txt.expandtabs(2)
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

# 8) find() Method
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("world")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e")
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

txt = "Hello, welcome to my world."
x = txt.find("p")
print(x)

# 9) format() Method
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print(txt1)
txt2 = "My name is {0}, I'm {1}".format("John",36)
print(txt2)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt3)

# :<
txt = "We have {:<8} chickens."
print(txt.format(49))

#:>
txt = "We have {:>8} chickens."
print(txt.format(49))

#:^
txt = "We have {:^8} chickens."
print(txt.format(49))

#:=
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

#:+
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

#:-
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

#:
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))

#:,
txt = "The universe is {:,} years old."
print(txt.format(13800000000))

#:_
txt = "The universe is {:_} years old."
print(txt.format(13800000000))

#:b
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

#:c

#:d
txt = "We have {:d} chickens."
print(txt.format(0b101))

#:e
txt = "We have {:e} chickens."
print(txt.format(5))

#:E
txt = "We have {:E} chickens."
print(txt.format(5))

#:f
txt = "The price is {:.2f} dollars."
print(txt.format(45))

txt = "The price is {:f} dollars."
print(txt.format(45))

#:F
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))

x = float('inf')
txt = "The price is {:f} dollars."
print(txt.format(x))

#:g

#:G

#:o
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))

#:x
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))

#:X
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))

#:n

#:%txt = "You scored {:%}"
print(txt.format(0.25))

txt = "You scored {:.0%}"
print(txt.format(0.25))

# 10) format_map() Method
myvar = {"name" : "John", "age" : 36}
txt = "Happy birthday {name} you are now on level {age}"
print(txt.format_map(myvar))

# 11) index() Method
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("d")
print(x)

txt = "Hello, welcome to my world."
print(txt[5:10])
x = txt.index("e", 5, 10)
print(x)

# 12) isalnum() Method
txt = "Company12"
x = txt.isalnum()
print(x)

txt = "Company 12"
x = txt.isalnum()
print(x)

txt = "Company/12"
x = txt.isalnum()
print(x)

txt = "Company@12"
x = txt.isalnum()
print(x)

txt = "Company&12"
x = txt.isalnum()
print(x)

# 13) isalpha() Method
txt = "CompanyX"
x = txt.isalpha()
print(x)

txt = "Company10"
x = txt.isalpha()
print(x)

# 14) isascii() Method

txt = "Company123"
x = txt.isascii()
print(x)

txt = "Company&"
x = txt.isascii()
print(x)

# 15) isdecimal() Method

txt = "1234"
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

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit())
print(b.isdigit())

# 17)  isidentifier() Method

txt = "Demo"
x = txt.isidentifier()
print(x)

a = "My Folder"
b = "Demo002"
c = "2bring"
d = "my_demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

# 18) islower() Method

txt = "hello world!"
x = txt.islower()
print(x)

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())
print(b.islower())
print(c.islower())

# 19) isnumeric() Method

txt = "565543"
x = txt.isnumeric()
print(x)

a = "10km2"
b = "-1"
c = "1.5"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
 
 # 20)  isprintable() Method

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)

# 21)  isspace() Method

txt = "   "
x = txt.isspace()
print(x)
txt = "   s   "
x = txt.isspace()
print(x)

# 22)  istitle() Method

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

# 23) isupper() Method

txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"
print(a.isupper())
print(b.isupper())
print(c.isupper())

# 24) join() Method

myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

myDict = {"name": "John", "country": "Norway"}
x = "TEST".join(myDict)
print(x)

# 25) ljust() Method

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

txt = "banana"
x = txt.ljust(20, "O")
print(x)

# 26) lower() Method

txt = "Hello my FRIENDS"
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

txt = "Hello Sam!"
mytable= str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(str.maketrans(x, y, z))

# 29) partition() Method

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I could eat bananas all day"
x = txt.partition("apples")
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

txt = "Hello, welcome to my world."
print(txt.rfind("q"))

txt = "Rishit/a"
print(txt.rfind("a"))

# 32) rindex() Method

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.rfind("q"))
print(txt.rindex("q"))

# 33) rjust() Method

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

txt = "banana"
x = txt.rjust(20, "O")
print(x)

# 34) rpartition() Method

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)

# 35) rsplit() Method

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

txt = "apple, banana, cherry"
x = txt.rsplit(", ", 1)
print(x)

# 36) rstrip() Method

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "banana,,,,,ssqqqww....."
y = txt.rstrip(",.qsw")
print(y)

# 37) split() Method

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "hello, my name is Peter, I am 26 years old"
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

# 39) startswith() Method

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)

txt = "Hi, welcome to my world."
x = txt.startswith(("Hello", "Hi"))
print(x)

# 40) strip() Method

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")


txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)

# 41) swapcase() Method

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

# 42) title() Method

txt = "Welcome to my world"
x = txt.title()
print(x)

txt = "Welcome to my 2nd world"
x = txt.title()
print(x)

txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)

# 43) translate() Method

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))

# 44) upper() Method

txt = "Hello my friends"
x = txt.upper()
print(x)

# 45) zfill() Method

txt = "50"
x = txt.zfill(10)
print(x)

a = "hello"
b = "welcome to the jungle"
c = "10.000"
print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

txt = """Manufacturing industries are central to employment, productivity, exports, and strategic resilience. They warrant a mission-oriented approach beyond incentive-based interventions, the Economic Survey 2025-2026 observed.In the midst of economic transformation, geopolitical uncertainty, and rapid technological change, manufacturing capacity needs to be viewed as a strategic national asset. And, MSMEs are crucial as they should evolve from micro-scale production to deeper participation in formal and export-linked supply chains.The next phase of industrialisation will require a calibrated shift from a model centred mainly on import substitution towards one focused on scale, competitiveness, innovation and deeper integration into GVCs.it noted."""
x = len()
print(x)