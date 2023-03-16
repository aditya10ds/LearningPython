# l1 = ["Harry","Sohan","Sachin","Rahul"]
# for name in l1 :
#     if name.startswith("S"):
#       print("Hello " + name)

num = int(input("Enter the number : "))
prime = True

for i in range(2, num) :
    if(num%i == 0):
        prime = False
        break
if prime:
        print("This number is prime ")
else:
        print("This number is not prime ")