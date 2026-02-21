#Python Operators

print(10 + 5)

sum1 = 100 + 50      
print(sum1)
sum2 = sum1 + 250   
print(sum2)
sum3 = sum2 + sum2  
print(sum3)

# 1) Python Arithmetic Operators

# + Addition
x = 5
y = 3
print(x + y) 

# -	Subtraction
x = 5
y = 3
print(x - y) 

# *	Multiplication 
x = 5
y = 3
print(x * y) 

# /	Division
x = 12
y = 3
print(x / y) 

# %	Modulus (................................................)
x = 5
y = 2
print(x % y) 

# ** Exponentiation 
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2=32

# // Floor division
x = 15
y = 2
print(x // y) 

x = 15
y = 4
print(x + y) 
print(x - y) 
print(x * y) 
print(x / y) 
print(x % y) 
print(x ** y) 
print(x // y) 

#Division in Python
x = 12
y = 5
print(x / y) 

x = 12
y = 5
print(x // y)

# 2) Assignment Operators

# =
x = 5
print(x) 

# +=
x = 5
x += 3
print(x) 

# -=
x = 5
x -= 3
print(x)

# *=
x = 5
x *= 3
print(x)

# /=
x = 5
x /= 3
print(x)

# %= (................................................)
x = 5
x %= 3
print(x)

# //=
x = 5
x //= 3
print(x)

# **=
x = 5
x **= 3
print(x)

# &= (................................................)
x = 5
x &= 3
print(x)

# |= (................................................)
x = 5
x |= 3
print(x)

# ^= (................................................)
x = 5
x ^= 3
print(x)

# >>= (................................................)
x = 5
x >>= 3
print(x)

# <<= (................................................)
x = 5
x <<= 3
print(x)

# :=
print(x := 3)

# 3) Python Comparison Operators

# == Equal
x = 5
y = 3
print(x == y)

# != Not equal
x = 5
y = 3
print(x != y)

# >	Greater than
x = 5
y = 3
print(x > y)

# <	Less than
x = 5
y = 3
print(x < y)

# >= Greater than or equal to (...........................................................................................)
x = 5
x = 5
y = 3
print(x >= y)

# <= Less than or equal to (...........................................................................................).)
x = 5
x = 5
y = 3
print(x <= y)

x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# 4) Python Logical Operators

# and 
x = 5
print(x > 3 and x < 10)
x = 5
print(x > 0 and x < 10)

# or
x = 5
print(x > 3 or x < 4)
x = 5
print(x < 5 or x > 10)

# not 
x = 5
print(not(x > 3 and x < 10))
x = 5
print(not(x > 3 and x < 10))

# 5) Python Identity Operators

# is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

# is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)

# Difference Between is and ==
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# 6) Python Membership Operators

# in
x = ["apple", "banana"]
print("banana" in x)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

# not in 
x = ["apple", "banana"]
print("pineapple" not in x)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

#Membership in Strings
text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

# 7) Python Bitwise Operators(...........................................................................................)

# & AND
print(6 & 3)

# |	OR
print(6 | 3)

# ^	XOR
print(6 ^ 3)

# ~	NOT
print(~3)

# << Zero fill left shift
print(3 << 2)

# >> Signed right shift
print(8 >> 2)

print(6 & 3)
print(6 | 3)
print(6 ^ 3)

# 8) Python Operator Precedence

print((6 + 3) - (6 + 3))

print(100 + 5 * 3)

# () Parentheses 
print((6 + 3) - (6 + 3)) #( 9 - 9 = 0)

# ** Exponentiation
print(100 - 3 ** 3) #100 - 27 = 73

# +x -x ~x Unary plus, unary minus, and bitwise NOT
print(100 + ~3) #100 + -4 = 96

# * / // % Multiplication, division, floor division, and modulus
print(100 + 5 * 3) #100 + 15 = 115

# + - Addition and subtraction
print(100 + 5 - 3) #100 + 5 - 3(2) = 102 

# << >> Bitwise left and right shifts
print(8 >> 4 - 2) # 8 >> 2 = 2

# &	Bitwise AND
print(6 & 2 + 1) # 6 & 3 = 2

# ^	Bitwise XOR
print(6 ^ 2 + 1) # 6 ^ 3 = 5

# |	Bitwise OR
print(6 | 2 + 1) #  6 | 3 = 7

# == != > >= < <=  is is not in not in  Comparisons, identity, and membership operators
print(5 == 4 + 1) # 5 == 5 = True

# not Logical NOT
print(not 5 == 5) #not True = False

# and AND (.................................................................................................................................)
print(1 or 2 and 3) # 1 or 3 = 1

# or OR	(...................................................................................................................................)
print(4 or 5 + 10 or 8) #4 or 15 or 8 = 4

# Left-to-Right Evaluation
print(5 + 4 - 7 + 3) #The calculation above reads: 5 + 4 = 9, 9 - 7 = 2, 2 + 3 = 5