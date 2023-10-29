# # val_int = "?"
# # if val_int == "+" or val_int =="-" :
# #     print("!!!")
# # else :
# #     print("??")
# #
# # ##not
# # if val_int is not True:
# #     print("Baby")
#
# # val =12
# # # if (val % 2) == 0 and (val % 5) ==0:
# # #     print(val)
# #
# # if not (val % 2) != 0 and not(val % 5) !=0:
# #     print(val)
#
# logged = True
# if not logged:
#     print("Please log in")
# else:
#     print("Welcome")
#
# a = 2000000
# b = 444
# # print("A") if a > b else print("B")
# result = True if a>b else False
# print(result)

#### while(True, flag value)

# value = 1
# while True:
#     value += 1
# print(value)

# value = 2
# while value < 10:
#     value += 1
#     print(value)

# value = 1 #####++++++++++++++++++++
# while value< 10:
#
#     value += 1
#     print(value)

# value = 1###### за флагом не сработало)
# is_true = True
# print(value)
# while is_true:
#        value += 1
# print(value)
# if value > 10:
#     is_true = False

###break , continue

# value = 1 #####++++++++++++++++++++
# while value < 10:
#  value += 1
#  if  value % 2:
#      continue
#  print(value)

# value = 1 #####++++++++++++++++++++
# while value < 10:
#  value += 1
#  if  value % 2:
#      continue
#  print(value)
# else:
#     print(value)
#     print("End")


### str method
# value ="Home"
# index= 2
# print(value[index])
###################  диапозон[2:4]
value ="Home"
## print(value[1:3])
# print(value[:])
# print(value[:-1]) # minus last symbol
# print(value _str[2:2;4])    # begining, end, крок
# print(value _str[::-1]) сконца перевернуто from the end
# print(value_str[::2])
# print(value_str[1::2])




# docum = "doc.py"
# dot =docum.find(".")
# print(dot)
# extention = docum[(dot):]
# print(extention)

# docum = "doc.py"
# dot =docum.find(".")
# print(dot)
# extention = docum[(dot+1):]
# print(extention)


# docum = "doc.py"
# # dot =docum.find(".")
# # print(dot)
# # extention = docum[:(dot)]
# # print(extention)#### name before dot
#
# print(len(docum))


# str_1 = "hello"
# str_2 = "Hello"
# if str_1.lower()== str_2.lower():
#     print("Thank you")

first_name = input("Insert your name:")
print(first_name.capitalize())