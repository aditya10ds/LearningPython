# n! = 1 x 2 x 3 x ..... x n 
# 5! = 1 x 2 x 3 x 4 x 5

num = int(input("Entr the number : "))
for i in range(num + 1):
  factorial = 1
  for i in range (1, num):
      factirial = factorial * i 
print(f"The factorial of this {num} is {factorial}")   