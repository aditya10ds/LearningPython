#Chatpter 3 Repeat 
a= 34
b= "Harry's" #use this if you have single quotes in your strings
b= ''''Harry"s and harry's'''   #use this if you have single quotes in your strings

# print(type(b))
print(a,b)

#string sclicing 
greeting = "Good Morning,"
name = "Harry"
print(type(name))
print(greeting+name ) #concatination strings 

c = greeting + name 
print(c)

name = "Aditya"
print(name[0])
print(name[1])
print(name[0:4])
print(name[0:6])
print(name [:6])
#name [3] = "d" #Does not work
print(name [-6:-1])
print(name [-1])

#sclicing with skip

print(name[1:5:3])

name= "AdityaIsGood"
d=name[0:14:2]
print(d)

#string Function

story= "once upon a time there was a Youtuber name Harry Who uploaded python course with notes"

print (story[0:15])
print (len(story))
print(story.endswith("notes"))
print(story.count("a"))
print(story.count("up"))
print(story.capitalize())
print(story.find("a"))
print(story.replace("Youtuber", "Batak"))

#Escape sequence characters
story= "once upon a time there was a Youtuber\n name \tHarry Who uploaded \python course\\ with notes"
print (story)
