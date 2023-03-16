 ## How STRIP works ?
# this = "     Aditya is a good    "
# # print(this)
# # # print(this.strip())

# Question number 7

def remove_and_split(string, word) :
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    Aditya is a good "
n = remove_and_split(this, "Aditya") 
print(n)   
    
