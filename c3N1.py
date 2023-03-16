# chapter 3 Strings
a= 34
b ="Aditya's" # use this if you have single quotes in your strings
b = '''aditya"s and
     aditya's ''' # use this if you have single quotes in your string aditya"s'''
print (a,b)
print (type(a))
print (type(b))

# String sclice 

greeting = "good morning, "
# name = "Aditya"
# print(type(name))
# c = greeting + name          #concatinating two string
# print (greeting + name )
# print(c)

name = "Aditya"
print(name[0])
print(name[1])
print(name[5])
# name [3]= "d"   ---> Does not work like this 

print (name[0:3]) # ---> this called sclicing

print (name[:3])   #is samr as name [0:3]
print (name[1:])    #is same as name [1:6]
print (name[1:6])

print (name [-1])    #this work from last letter 
print (name [-6:-3])   # this is as name [0:3]
print (name [0:3])

# Slicing with skip value 
d = name [1:6:2]

print (d)

Name = "AdityaIsGood"
e = Name [0::3]
print (e)
