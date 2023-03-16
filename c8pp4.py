
def sum_recursive(n):
    if n <= 1 :
       return n
    else :
       return sum_recursive(n-1) + n

s = int(sum_recursive(6))
print(s)