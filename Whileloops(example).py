#Python While Loops

i = 1
while i < 6:
  print(i)
  i += 1

i = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
while i < 6:
  print(i)
  i += 1

avdi_gyu = 'na'

# for i in range(10):
#     print("home work karo",i+1)

while avdi_gyu == 'na':
    studetns = input("aavadyu k nai :- ")
    if studetns == 'ha':
        avdi_gyu = 'ha'


#while loops example(Office)

#1
age = 20
while age < 25:
   print(age)
   age += 1

#2
# travel = "yes"
# while travel == "yes":
#    person = input("you want to travel?")
#    print(person)
#    if person == "no":
#         break

#3
Player = "Alive"
while Player == "Alive":
  game = input("are you playing game?")
  print(game)
  if game == "no":
     print("player is dead")
     break


