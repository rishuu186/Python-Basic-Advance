# # list = input("mummy su su lavu che?")
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


#2)
asking_mom = input("mummy su su lavu che?")
Shooping_list = asking_mom.split(",")
print(Shooping_list)
asking_mom = "na"
#sugar, tea, milk ,rice ,garam mashala ,butter Milk 

asking_mom = input("List barabar che ?")   
if asking_mom == "ha":
    print("ok")
elif asking_mom == "na":
    while asking_mom == "na":
        asking = input("you want to add or remove something?")
        print(asking)
        if asking == "add":
            add_item = input("what?")
            Shooping_list.append(add_item)
            print(Shooping_list) 
        elif asking == "remove":
            remove_item = input("what?")
            Shooping_list.remove(remove_item)
            print(Shooping_list)
        else:
            print("wrong input")
        asking_mom = input("List barabar che ?")  
        if asking_mom == "ha":
            print("hiiii,okayy")

