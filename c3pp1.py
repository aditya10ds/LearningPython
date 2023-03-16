#  PRACTICE SET CHAPTER 3

# a= " name "
# print(input(a))

# name = aditya    ------. Mistake 

# print ("name ")

# Question 1

name = input("Enter your name:")
a= "Good Morning, "
print( a + name)

# Question 2

letter = '''Dear <| NAME |>
            Your are selected !!
            <| DATE |>'''

name = input("Enter your Name\n")
date = input("Enter your Date\n ")
letter = letter.replace("<| NAME |>", name)
letter = letter.replace(" <| DATE |>", date)
print (letter)

#Question 3 

st = "This is a string with double  spaces"
doubleSpaces =  st.find("  ")
print(doubleSpaces)


#Question 4

st = "This is a string with double  spaces"
doubleSpaces =  st.replace("  "," ")
print(doubleSpaces)


#Question 5 
 
letter = "Dear Harry,\nThis Python Course is nice. Thanks "
print(letter)

