def game():
    return 6444

score = game()
with open("c9pp2sample.txt") as f :
    highscoreStr = (f.read())
if highscoreStr =="" :
    with open("c9pp2sample.txt", "w") as f :
             f.write (str(score)) 

         
elif int(highscoreStr) < score :
    with open("c9pp2sample.txt", "w") as f :
             f.write (str(score))