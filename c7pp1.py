# Get the number from the user
num = int(input("Enter the number for multiplication table: "))

# Using for loop to print multiplication table
for i in range(1, 11):
    print(num, "x", i, "=", num*i)
