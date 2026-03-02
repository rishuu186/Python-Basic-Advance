#Python If Else Statement

#1) Python If Statement

a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 30
if b > a:
  print("b is greater than a")
elif a > b:
  print("b is not greter than a")

a = 8585
b = 8585
if a == b:
  print("a and b are Equal")

a = 8456
b = 4856
if a != b:
  print("a and b are not equal")

a = 56
b = 52
if a > b:
  print("a is greater than b")

a = 80
b = 85
if a < b:
  print("b is greater than a")

number = 15
if number > 0:
  print("The number is positive")

number = 1864
if number >= 1864:
  print("Less than or equal to")

number = 9642
if number <= 9642:
  print("Greater than or equal to")

# Multiple Statements in If Block
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

score = 95
if score >= 90:
  print("Congo You Are in top 3")
  print("your rank is 2nd")
  print("you're doning good in study")

age = 85
if age >= 80:
  print("you have to maintain your body")
  print("you have to eat healthy food")
  print("make sure you sleep on time")

score = 25
if score <= 30:
  print("you need to improve your study")
  print("you should study atlest 4 hr in day")
  print("otherwise you're study performence will go low")

age = 20
if age >= 18:
  print("you are a teenager")
  print("you can have a license")
  print("you can drive ")

# Using Variables in Conditions
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

is_logged_out = True
if is_logged_out:
  print("successfully logged out! ")

variable_condition = True
if variable_condition:
  print("you can use any variable")

username = True
if username:
  print("username:python")

password = True
if password:
  print("ri****@***7")

#2) Python Elif Statement

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 8585
b = 8585
if a != b:
  print("a and b are not Equal")
elif a == b:
  print("a and b are Equal")

a = 8456
b = 4856
if a == b:
  print("a and b are equal")
elif a != b:
  print("a and b are not equal")


a = 56
b = 52
if a > b:
  print("a is greater than b")
elif a < b:
  print("b is greater than a")

a = 80
b = 85
if a > b:
  print("a is greater than b")
elif a < b:
  print("b is greater than a")

number = 15
if number > 20:
  print("The number is negative('greater')")
elif number < 20:
   print("The number is positive")

#Multiple Elif Statements
score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

month = 12
if month == 1:
  print("January")
if month == 2:
  print("February")
if month == 3:
  print("March")
if month == 4:
  print("April")
if month == 5:
  print("May")
if month == 6:
  print("June")
if month == 7:
  print("July")
if month == 8:
  print("August")
if month == 9:
  print("September")
if month == 10:
  print("October")
if month == 11:
  print("November")
if month == 12:
  print("December")

day = 7
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

age = 18
if age < 1:
 print("You are a New born")
elif age < 13:
 print("You are a Child")
elif age < 19:
 print("You are a Teenager")
elif age < 30:
 print("You are a Young")
elif age < 50:
 print("You are an Adult")
elif age >= 65:
 print("You are a Senior")

#3) Python Else Statement

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

age = 36
if age < 19:
 print("You are a Teenager")
elif age < 35:
 print("You are a Young")
else:
 print("You are a Senior")

marks = 89
if marks > 80 :
  print("Topper")
elif marks > 30 :
  print("Normal")
else:
  print("Fail")

price = 49
if price > 100:
  print("High")
elif price > 50:
  print("Medium")
else:
  print("Low")

#Else Without Elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

marks = 85
if marks >= 20:
  print("PAAS")
else:
  print("FAIL")

tmp = 20
if tmp < 10:
  print("it's Cold Outside")
else:
  print("it's warm outside")

age = 39
if age >= 40:
  print("Senior")
else:
  print("Adult")

price = 89
if price > 100:
  print ("High Price")
else:
  print("Low Price")

number = 25
if number % 2 == 0:
  print("number is even")
else:
  print("number is odd")

#Complete If-Elif-Else Chain
temperature = 22
if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

marks = 29
if marks > 90:
  print("Grade A")
elif marks > 80:
  print("Grade B")
elif marks > 50:
  print("Grade C")
elif marks >= 30:
  print("FAIL")
else:
  print("Need Improvement")

a = 721
b = 721
if a > b:
  print("A id greater than B")
elif a < b:
  print("B is Greater Than A")
else:
  print("a and b Are Equal")

price = 49
if price > 100:
  print ("High Price")
elif price > 50:
  print("Medium Price")
else:
  print("Low Price")

#Else as Fallback (.....................................................................................................)

username = "Emil"
if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

#4) Python Shorthand If

a = 200
b = 33
if a > b: print("a is greater than b")

marks = 85
if marks > 80: print("Grade A")

price = 101
if marks > 100: print("High Price")

temperature = 31
if temperature > 30: print("It's hot outside!")

age = 54
if age >= 40: print("Senior")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

marks = 85
print("PAAS") if marks >= 20 else print("FAIL")

tmp = 20
print("Cold Outside") if tmp < 10 else print("Warm outside")

age = 39
print("Senior") if age >= 40 else print("Adult")

price = 89
print ("High Price") if price > 100 else print("Low Price")

number = 25
print ("even") if number % 2 == 0 else print("odd")

#Assign a Value With If ... Else (.................................................................)
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#Multiple Conditions on One Line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 721
b = 721
print("A > B") if a > b else print("B > A") if a < b else print("A = B")

price = 49
print ("High") if price > 100 else print("Medium") if price > 50 else print("Low")
  
marks = 29
print("Grade A") if marks > 90 else print("Grade B") if marks >= 30 else print("FAIL")

tmp = 2
print("Hot outside!") if tmp > 30 else print("Warm outside") if tmp > 20 else print("cool outside") if tmp > 10 else print("cold outside!")

#Example(.............................................................................................................................)
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

#5) Python Logical Operators

#The and Operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 20
b = 20
c = 500
if a < c and a == b:
  print("only one condition is ture")

#Example(office)
a = 25
b = 58
if a > b:
    print("a is greter than b")
elif a < b:
    print("b is greter than a")
elif a == b:
    print("a is equals to b")
else: 
    print("a != b")


makrs = 92
if makrs >= 90:
    print("Grade A")
    if makrs >95:
     print("Excellent")
    else:
     print("very very good")
elif makrs >= 80:
    print("Grade B")
    if makrs >85:
     print(" very Goodd")
    else:
     print("good")
elif makrs >= 70:
    print("Grade C")
    if makrs >75:
     print("Need Focus")
    else:
     print("improve yourself")
elif makrs >= 30:
    print("Grade D")
    if makrs >35:
     print("need improvement")
    else:
     print("Daily 5hr of study")
else:
    print("Fail")