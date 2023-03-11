 # DICTIONARY & SETS 

myDict = {
    "Fast" : "In a Quick Manner",
    "Harry" : "A Coder",
    "Marks" : [1, 2, 50 ],
    "anotherdict" : {"harry" : 'player'}
}

# print(myDict["Fast"])
# print(myDict["Harry"])
myDict["Marks"] = [ 45, 78]
print(myDict["Marks"])
print(myDict["anotherdict"])
print(myDict["anotherdict"] ["harry"])

# Dictonary methods 

myDict = {
    "fast" : "In a Quick Manner",
    "harry" : "A Coder",
    "marks" : [1, 2, 50 ],
    "anotherdict" : {"harry" : 'player'},
    1 : 2
}
 
print(list(myDict.keys())) # prints the keys of the dictonary 
print(list(myDict.values()))  # prints the keys of the dictonary
print(list(myDict.items()))  # prints the keys , Values for all contents in  the dictonary

print(myDict)
updateDict = {
    "Lovish" : "Friend", 
    "Aadu" : "Paddu",
    "harry" : "the dancer "
                                    
}
myDict.update(updateDict)  #--------------------> Update the dictonary with by adding key- value  from .update

print(myDict)
print(myDict.get("harry"))      #----------------> print value associated with key "harry"
print(myDict["harry"])

# The diffrenec between .get and [] sytax in dictonaries ?
print(myDict.get("harry2"))     #--------------> return None as harry2 is not present in the dictonary 
print(myDict['harry2'])         #Throws an error s harry2 is not present in the dictonary 


 #                Sets 
 
a = { 1, 3, 4, 5}
print(a) 




