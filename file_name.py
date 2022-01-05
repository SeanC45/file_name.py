while True:
    def Player_One ():
        input ("Please select your Pick, Player_One: ")
    def Player_Two ():
        input ("Please select your Pick, Player_Two: ")
    quit = input ("Type 'Play' to Play or 'Stop' to end game:")
    
    if (Player_One()== "Rock")and (Player_Two()== "Scissor"):
        print ("Player One is the WINNER!!")
    elif (Player_One()== "Scissor") and (Player_Two()== "Paper"):
        print ("Player One is the WINNER")
    elif (Player_One()== "Paper") and (Player_Two()== "Rock"):
        print ("Player Two is the WINNER")
    elif (Player_One()== "Rock") and (Player_Two()== "Paper"):
        print ("Player One is the WINNER")
    elif (Player_One()== "Paper") and (Player_Two()== "Scissor"):
        print ("Player One is the WINNER")
    else:
        Print ("Draw - No win :(" + "\n"+ quit)
        Player_One
        Player_Two
