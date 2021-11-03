#Import dependencies
import os
import time
import matplotlib

#Import the other project filess
import functions.game as gameModule
import functions.ai as aiModule

#a function to clear the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Game engine (main program)
#create a game object
game = gameModule.Game()
game.draw()

    #take in game parameters

    #start the game (while loop)
        #draw board
        #player1 makes move
        #check for win
        #draw board
        #player2 makes move
        #check for win
