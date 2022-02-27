#This is our project for HakD
#Scenerio 1
#The game is Connect 4
#Meant for PVP

# Libs
# Art Library for some fancy ASCII texts (installed using pip) (art, version 5.4)
import art as a
#Time
import time as t
# Colored text
from colorama import Fore as color
# pygame for sound
import pygame
pygame.init()
pygame.mixer.init()
GOsound = pygame.mixer.Sound('Mario death.mp3')
SFX = pygame.mixer.Sound('SFX for Connect 4.mp3')
music = pygame.mixer.Sound('bensound-dreams (2).mp3')
music.play(loops=-1)

# Set Variables
pos = [5,5,5,5,5,5,5] # This is the position where the token can be placed in each colum (0 is at the top so we have to use 5)
grid = [[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]
# In the grid, 0 is empty, R is red and Y is yellow
gameStop = False
winner = ''

# Intro Section Start

def intro():
    loadingScreen()
    welcomeText()

# "Loading Screen"
def loadingScreen():
    print(color.BLUE)
    a.tprint("Connect 4")
    t.sleep(1)
    print(color.CYAN + "Version 1.0")
    print("Music: www.bensound.com")
    t.sleep(1)
    print("Loading...")
    t.sleep(3)
    print(color.GREEN)
    print("A project of HakD 2022:")
    t.sleep(1)
    a.tprint("Game On",font = "tarty1")
    t.sleep(2)
    print(color.RESET)
    print() # leave a gap

# Welcome Text
def welcomeText():
    print("Hello World!")
    t.sleep(1)
    print("This is a digital version of Connect 4, meant for two players.")
    t.sleep(2)
    print("Standard Connect 4 rules.")
    t.sleep(2)
    print("Enjoy and Game On!")

# Intro section End

# Game Section Start

def game():
    print("The Game Starts.")
    t.sleep(1)
    while True:
        print(color.YELLOW + "Yellow's turn.")
        onePlayer("Yellow")
        if checkStop() != "No":
            return checkStop()
        print(color.RED + "Red's turn.")
        onePlayer("Red")
        if checkStop() != "No":
            return checkStop()


def onePlayer(color):
    print("This is the current grid.")
    printGrid()
    success = False
    while(success == False):
        while True:
            choice = input("Please enter the number of the colum you want to put your piece in (Left-most is 1, Right-most is 7): ")
            if choice.isdigit():
                choice = int(choice)
                choice = choice - 1
                if choice < 0 or choice > 6:
                    print("Your input is invalid. Please try again.")
                else:
                    break
            else:
                print("Your input is invalid. Please try again.")
        if check(choice):
            placePiece(choice, color)
            print("Your piece has been placed.")
            success = True
        else:
            print("That colum is full and your piece cannot be placed. Please try again.")



def printGrid():
    for i in range(6):
        print(color.GREEN + "->",color.BLUE + "   | ",end='')
        for j in range(7):
            if grid[i][j] == 0:
                print(" ",end = ' | ')
            elif grid[i][j] == "Y":
                print(color.YELLOW + "●",end=color.BLUE + ' | ')
            else:
                print(color.RED + "●",end=color.BLUE + ' | ')
        print()
    print(color.GREEN + "->", "     ", end='')
    for i in range(7):
        print(color.CYAN + str(i + 1),end='   ')
    print(color.RESET)



def placePiece(x,color):
    if color == "Yellow":
        grid[pos[x]][x] = "Y"
        pos[x] -= 1
    else:
        grid[pos[x]][x] = "R"
        pos[x] -= 1
    SFX.play()

def check(x):
    if pos[x] >= 0: # colum is not full
        return True
    return False

# Win Check Section Start

def checkStop():
    if checkWin() != "No":
        if checkWin() == "Y":
            return "Y"
        if checkWin() == "R":
            return "R"
        else:
            return "Draw"
    return "No"

def checkWin():
    for x in range(7):
        for y in range(7):
            for turn in ['Y', 'R']:
                try:
                    # Sideways line checking
                    if grid[x][y] == turn and grid[x][y + 1] == turn and grid[x][y + 2] == turn and grid[x][y + 3]: pass
                except:  # In case of a RangeError, meaning it checks for Board off the edge of the board
                    pass
                else:
                    if grid[x][y] == turn and grid[x][y + 1] == turn and grid[x][y + 2] == turn and grid[x][y + 3] == turn:
                        return turn
                try:  # Diagonal-right check
                    if grid[x][y] == turn and grid[x + 1][y + 1] == turn and grid[x + 2][y + 2] == turn and grid[x + 3][y + 3]: pass
                except:
                    pass
                else:
                    if grid[x][y] == turn and grid[x + 1][y + 1] == turn and grid[x + 2][y + 2] == turn and grid[x + 3][y + 3] == turn:
                        return turn
                try:  # Vertical Check
                    if grid[x][y] == turn and grid[x + 1][y] == turn and grid[x + 2][y] == turn and grid[x + 3][y]: pass
                except:
                    pass
                else:
                    if grid[x][y] == turn and grid[x + 1][y] == turn and grid[x + 2][y] == turn and grid[x + 3][y] == turn:
                        return turn
                try:  # Diagonal-left check
                    if grid[x][y] == turn and grid[x - 1][y + 1] == turn and grid[x - 2][y + 2] == turn and grid[x - 3][y + 3]: pass
                except:
                    pass
                else:
                    if grid[x][y] == turn and grid[x - 1][y + 1] == turn and grid[x - 2][y + 2] == turn and grid[x - 3][y + 3] == turn:
                        return turn
    for i in range(6):
        for j in range(7):
            if grid[i][j] == 0:
                return "No" # Checks for Tie (if there is any empty spaces in the top row after checking for a win)
    return "Draw"
#Win Check section End
#Game Section End




#Conclusion
def conclusion(winColor):
    printGrid()
    print(color.GREEN)
    music.fadeout(1)
    GOsound.play()
    a.tprint("Game Over",font="georgia11")
    t.sleep(2)
    print(color.RESET)
    music.play(loops=-1)
    if winColor == "R":
        print("The winner is...")
        t.sleep(1)
        print(color.RED + "RED!")
    if winColor == "Y":
        print("The winner is...")
        t.sleep(1)
        print(color.YELLOW + "YELLOW!")
    if winColor == "Draw":
        print("The Game is a DRAW.")
    t.sleep(2)
    print(color.RESET + "Thank you for playing this game.")
    t.sleep(1)
    choice = input("Would you like to play one more round? (Y/Anything Else):  ")
    if choice == "Y" or choice == "y":
        print("Starting Next Round...")
        t.sleep(3)
        return True
    else:
        print("Goodbye!")
        return False



#Main Code
oneMoreRound = True
2
intro()
t.sleep(1)
while oneMoreRound:
    pos = [5, 5, 5, 5, 5, 5, 5]
    grid = [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
    gameStop = False
    winner = game()
    oneMoreRound = conclusion(winner)


