import random

def gameWin(comp, you):
    if you not in ["s", "w", "g"]:
        return None
    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True

print("comp Turn : Snake(s) water(w) or gun(g) ?")
randomNo = random.randint(1, 3)

if randomNo == 1:
    comp = "s"
elif randomNo == 2:
    comp = "w"
elif randomNo == 3:
    comp = "g"

you = input("Your Turn : Snake(s) water(w) or gun(g) ?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
