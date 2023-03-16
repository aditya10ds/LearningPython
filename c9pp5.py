words = ["donkey", "kaddu", "mote"]

with open("c9sample.txt") as f:
    content = f.read()
for word in words:
    content= content.replace(word, "$$%^$$#")    


with open("c9sample.txt", "w") as f:
     f.write(content)