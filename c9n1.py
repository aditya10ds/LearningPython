# Use  open function to read the content of a file !
# f= open('c9sample.txt', 'r')
f= open('c9sample.txt',) #by default the mode is r
# data = f.read()
data = f.read(5)
print(data)
f.close()

