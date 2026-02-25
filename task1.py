list = input("mummy su su lavu che?")
Shooping_list = list.split(",")
print(Shooping_list)
#sugar, tea, milk ,rice ,garam mashala ,butter Milk 

Mummy = input("List barabar che ?")
if Mummy == "ha":
    print("ok")
elif Mummy == "na":
    a = input("you want to add or remove something?")
    print(a)
    if a == "add":
        b = input("what?")
        Shooping_list.append(b)
        print(Shooping_list) 
    elif a == "remove":
        x = input("what?")
        Shooping_list.remove(x)
        print(Shooping_list)
    else:
        print("wrong input")

