import random

def game():
    print("You are playing  a Game")
    score=random.randint(1,50)
    #Fetch the hiscore
    with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\hiscore.txt","r") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0    


    print(f"you score : {score}")
    if(score>hiscore):
        with open(r"C:\Users\sbbra\OneDrive\Desktop\Python\Chapter 9-PS\hiscore.txt","w") as f:
            f.write(str(score))

        return score    

game()