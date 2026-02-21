#Python Data Types 

# 1) Text Type 
x = str("Hello World")
print(x)
y = "Hello World"
print(type(y))

# 2) Numeric Type

#Integer 
x = int(18)
print(x)
y = 18
print(type(y))

#Floating Number
x = float(22.0)
print(x)
y = 32.3
print(type(y))

#Complex Number
x = complex(1j)
print(x)
y = 1j
print(type(y))

# 3) Sequence Type

#list
x = list(("apple","banana","cherry"))
print(x)
y = (("apple","banana","cherry"))
print(type(y))

#Tuple
x = tuple(("apple","banana","cherry"))
print(x)
y = (("apple","banana","cherry"))
print(type(y))

#Range
x = range(8)
print(x)
print(type(x))

x = list(range(6))
print(x)

# 4) Mapping Type

#Dictionary
x = dict(name="Rishita",age=21)
print(x)
print(type(x))

# 5) Set Type

#Set
x = set(("apple","banana","cherry","apple"))
print(x)
y = (("apple","banana","cherry","apple"))
print(type(y))

#Frozenset
x = frozenset(("apple","banana","cherry"))
print(x)
y = (("apple","banana","cherry"))
print(type(y))

# 6) Boolean Type

x = bool(True)
print(x)
y = False
print(type(y))

# 7) Binary Types

# Bytes
x = bytes(5)
print(x)
print(type(x))

b = b"RI"
print(b[0])
print(type(b))

# BytesArray
x = bytearray(3)
print(x)
print(type(x))

# MemmoeryView
x = memoryview(bytes(5))
print(x)
print(type(x))

# 8) None Type

x = None
print(x)
print(type(x))