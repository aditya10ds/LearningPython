       # Sets 
a = { 1, 3, 4, 5,1}
print(a) 
print(type(a))

# Imposrtant : this syntax will create an empty dictonary and not an empty set
a= {}
print(type(a))   

# An empty set can be crated using the below syntax :

b = set()
print(type(b))

# Adding the value to an empty sets 
b.add(4)
b.add(5)
b.add(4)           # Adding a value repeatedly does not changes a sets 
b.add((4, 5, 6))   # Cannot Add list or dictonary to Sets but tuple can be added 
# b.add({4:5})        # Cannot Add list or dictonary to Sets

print (b)

## Length of the sets 
print (len(b))

## Removal of an items 
b.remove(5)     # removes 5 from set b 
# b.remove(15)  # throes an while trying to remove 15 ( which is not present in the set)
print(b)

print(b.pop())
print(b)
print(b.clear())
print(b)
   

