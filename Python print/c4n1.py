 #Chapter 4 List and tulips 
 
 #Create a list using []

a= [1,2,3,4,5,55]
# print the list using print () function
print (a)

# Access using index using a[0], a[1], a[2]
print(a[2])
# Change the value of list using 
a[0] = 98
print(a )

# we can create a list with items of different types

c = [ 45, "harry0 " , False , 6.9]
print(c)

# List Sclicing

friends = ["harry", "tom", "Rohan","Sam", "Divya" , 45 ]
print(friends[0:4])
print(friends[-4:])
print(friends[0:1:4])

#List Method

l1 = [1, 8, 7, 2, 21, 15]
# li1_sorted= l1.sort()
# print(li1_sorted) --------> Wrong Method
# l1.sort()   #--------> its works Arrangments 
# print(l1)
#l1.reverse()   # Reverse the list 

# l1.append(45)
# l1.append(85)   #adds at the end of the list 
# l1.insert(2,544)   #insert 544 at index 2 

# l1.pop(2)      #remove element at index 2
  
# l1.remove(21)    #Remove 21 from the list 

print(l1)




             # TUPLE METHOD 

t = (1, 2, 4, 5)
# t1 = ()  # empty tuple 
# t1 =(1) #Wrong way to declare a tuple with Single element
t1 = (1,) #tuple with single element

print(t1)

# Printing the elemnt if a tuple
# print(t[0])


#cannot update the values of a tuple
# t[0] = 34  # throw an error 

# Method of tuples
t = (1, 2, 4, 5, 4, 1, 2, 1, 1,1)

print(t.count(1))
print(t.index(1))
print(t.index(5))









