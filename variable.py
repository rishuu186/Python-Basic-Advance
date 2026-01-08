# Python Variable (containers for storing data values)
x = 18
y = "Python"
#print(x)
#print(y)

x = 18
y = "Python"
#print(x),print(y)

x = 18
y = "Python"
#print(x,y) 

# You can't 
x = 18
y = "Python"
#print(x)(y)


# Change the type even after they have been set
x = 18
x = "Python"
#print(x)


# Casting(Specify the data type) 
x = str(8)
y = int(8)
z = float(8)
#print(x),print(y),print(z)


# Get the type of a function 
x = 18
y = "Python"
#print (type(x)),print (type(y))


# Single or Double Quotes (declare by both)
x = "Python"
y = 'Python'
#print(x),print(y)

# Case Sensitive (variables names are case sensitive)
a = 18 
A = "Python"
#print(a),print(A)

# Variable Names (Legal Variable)
Myvar = 18
myVar = 18 
_my_var = 18 
my_var = 18
myvar2 = 18 
my2var = 18
#print(Myvar),print(myVar)
#print(_my_var),print(my_var)
#print(myvar2),print(my2var)

# (illegal Variable Names)
#2myvar = 18
#my-var = 18
#my var = 18
#print(2myvar),print(my-var),print(my var)

# Camel Case (Each Word, Except The First,Start With A Capital Latter)
myVariableName = "Camel Case"
#print(myVariableName)

# Pascal Case (Each Word Starts With Capital Letter)
MyVariableName = "Pascal Case"
#print(MyVariableName)

# Snake Case (Each Word Is Separeted By An Underscore(_))
My_Variable_Name = "Snake Case"
my_variable_name = "snake case"
#print(My_Variable_Name),print(my_variable_name)





#Assign Multiple Values

# 1) Many Values To Multiple Variables
x , y , z = "Orange" , "Banana" , "Cheery"
#print(x),print(y),print(z)

# 2) One Values To Multiple Variables
x = y = z = "orange"
#print(x),print(y),print(z)

# 3) Unpacking a Collection
Fruits = ["Apple","Banana","Cheery"]
x,y,z= Fruits
print(x),print(y),print(z)



