import random 
l=["rock", "scissor", "paper"]

while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game start...
1 Yes
2 No | Exit
             '''))
    
    if uc ==1:
        for a in range(1,6):
            userInput=int(input('''
1 Rock
2 scissor 
3 Paper                             

                                '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            # print(uchoice)
            # print(Cchoice)
            if Cchoice==uchoice:
                print("Computer Value",Cchoice)
                print("Computer Value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif((uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or
            (uchoice=="scissor" and Cchoice=="paper" )) :
                print("Computer Value",Cchoice)
                print("Computer Value",uchoice)
                print("you Win")
                ucount=ucount+1
            else:
                print("Computer Value",Cchoice)
                print("Computer Value",uchoice)
                print("computer Win") 
                ucount=ucount+1 

        if ucount==ucount :
            print("final Game Draw ...")
            print("User Score ", ucount)
            print("Computer Score", ccount)
        elif(ucount >ccount):
            print("final you win the Game ...")
            print("User Score ", ucount)
            print("Computer Score", ccount)   
        else:
            print("computer Win the game ....")
            print("User Score ", ucount)
            print("Computer Score", ccount)              



    else:
        break    

