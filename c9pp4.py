with open("c9sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$$%^$$#")    
with open("c9sample.txt", "w") as f:
     f.write(content)