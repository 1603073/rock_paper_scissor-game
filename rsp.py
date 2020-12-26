from random import randint
t = ["rock","scissor","paper"]
computer = t[randint(0,2)]
player = False

while player == False:
    player = input("what's your hit? rock, paper or scissor?")
    if player == computer:
        print("It's a tie")
   
    elif player == "rock":
        if computer == "scissor":
            print(player,"win!",player,"beats",computer)
        else:
            print(player,"lose!",computer,"beats",player) 

    elif player == "scissor":
        if computer == "paper":
            print(player,"win!",player,"beats",computer)
        else:
            print(player,"lose!",computer,"beats",player)   

    elif player == "paper":
        if computer == "rock":
            print(player,"win!",player,"beats",computer)
        else:
            print(player,"lose!",computer,"beats",player)  

    else:
        print("U have given a wrong input!please try again!!!...")

    player = Fals
    computer = t[randint(0,2)]            
