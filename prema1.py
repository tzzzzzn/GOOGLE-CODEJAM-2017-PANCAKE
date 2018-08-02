import sys
from random import randint
from time import sleep
from copy import deepcopy
#Setup game
def main():
    #Set default board values
    global p,c
    if(int(input('select which symbol you want to use 1. X  2. O'))==1):
        p=" X "
        c=" O "
    else:
        p=" O "
        c=" X "
    global board
    board = [[0, "  "], [1, "  "], [2,"  "], [3,"  "], [4,"  "], [5,"  "], [6,"  "], [7,"  "], [8,"  "]]
    #Sets default counter value:
    global counter
    counter = 0
    #Calls function to draw board
    drawBoard()
    return
#Draw game board
def drawBoard():
    #Draws game board with proper variables
    print(board[0][1] + "|"+ board[1][1] +"|" + board[2][1] + "\n---+---+--- \n" + board[3][1] +"|" + board[4][1] + "|"
          + board[5][1] + "\n---+---+--- \n" + board[6][1] + "|" + board[7][1] + "|" +  board[8][1] + "\n")
    print(board[0][0] , "|", board[1][0] ,"|" , board[2][0] , "\n---+---+--- \n" , board[3][0] ,"|" , board[4][0] , "|",
        board[5][0] , "\n---+---+--- \n" , board[6][0] , "|" , board[7][0] , "|" ,  board[8][0] , "\n")
    #After board has been updated, initiates next turn
    nextTurn(counter)
    return
#Execute the next turn    
def nextTurn(count):
    #If count is divisible by two, let the player make a move and increase turn counter
    if count % 2 == 0:
        global counter
        counter += 1
        playerMove()
    #If count is not divisible by two, let the cmputer make a move and increase turn counter
    else:
        counter += 1
        computerMove()
#Code for the player's move
def playerMove():
    global n
    #Get player input and try to convert it to an integer.  If it cannot be, prompt user to enter again
    try:
        boardSpot = int(input("It's your turn! Please select an empty space on the board by typing a number 0-9\n"))
    except ValueError:
        playerMove()
    #If the space is empty, proceed
    if(n==1):
        if board[boardSpot][1] != p and board[boardSpot][1] != c :
            #Set board spot to X and redraw the board
            board[boardSpot][1] = p
            if checkWinner(board, p) == True:
                print("You have won! \n")
                endOfGame()
                return
            k=checkTie(board)
            if(k==0):
                return
            drawBoard()
            #Else, let them input a new number by recalling playerMove 
        else:
            playerMove()
    elif(n==2):
        if board[boardSpot][1] != p and board[boardSpot][1] != c :
            #Set board spot to X and redraw the board
            board[boardSpot][1] = p
            if checkWinnerrr(board, p) == True:
                print("You have won! \n")
                endOfGame()
                return
            k=checkTie(board)
            if(k==0):
                return
            drawBoard()
            #Else, let them input a new number by recalling playerMove 
        else:
            playerMove()
    elif(n==3):
        if board[boardSpot][1] != p and board[boardSpot][1] != c :
            #Set board spot to X and redraw the board
            board[boardSpot][1] = p
            if checkWinnerrrrr(board, p) == True:
                print("You have won! \n")
                endOfGame()
                return
            k=checkTie(board)
            if(k==0):
                return
            drawBoard()
            #Else, let them input a new number by recalling playerMove 
        else:
            playerMove()
def computerMove():
    #Display some dialouge alerting the user that the computer is making its move
    print("It's the computer's Turn!")
    sleep(1)
    print("Thinking...")
    sleep(1)
    global n
    #For loop iterating through every board spot.  Checks to see if bot can win.  If it can, make that winning move!
    for boardSpot in range (0,9):
        #Makes a copy of the board
        boardCopy = deepcopy(board)
        #If boardspot is empty, continue with the check.  Else, move onto the next spot!
        if(n==1):
            if boardCopy[boardSpot][1] != p and boardCopy[boardSpot][1] != c:
                boardCopy[boardSpot][1] = c
                if checkWinner(boardCopy, c):
                    board[boardSpot][1] = c
                    print("You have lost to the bot! \n")
                    endOfGame()
                    return
                    drawBoard()
                    return
        elif(n==2):
            if boardCopy[boardSpot][1] != p and boardCopy[boardSpot][1] != c:
                boardCopy[boardSpot][1] = c
                if checkWinnerr(boardCopy, c):
                    board[boardSpot][1] =c
                    print("You have lost to the bot! \n")
                    endOfGame()
                    return
                    drawBoard()
                    return
        elif(n==3):
            if boardCopy[boardSpot][1] != p and boardCopy[boardSpot][1] != c:
                boardCopy[boardSpot][1] = c
                if checkWinnerrrr(boardCopy, c):
                    board[boardSpot][1] = c
                    print("You have lost to the bot! \n")
                    endOfGame()
                    return
                    drawBoard()
                    return
    #For loop iterating through every board spot.  Checks to see if player can win.  If it can, prevent him from winning!
    for boardSpot in range(0,9):
        #Makes a copy of the board 
        boardCopy = deepcopy(board)
        #If boardspot is empty, continue with the check.  Else, move onto the next spot!
        if(n==1):
            if boardCopy[boardSpot][1] != p and boardCopy[boardSpot][1] != c:
                boardCopy[boardSpot][1] = p
                if checkWinner(boardCopy, p):
                    board[boardSpot][1] = c
                    drawBoard()
                    return
        elif(n==2):
            if boardCopy[boardSpot][1] != p and boardCopy[boardSpot][1] != c:
                boardCopy[boardSpot][1] = p
                if checkWinnerr(boardCopy, p):
                    board[boardSpot][1] = c
                    drawBoard()
                    return
        elif(n==3):
            if boardCopy[boardSpot][1] != p and boardCopy[boardSpot][1] != c:
                boardCopy[boardSpot][1] = p
                if checkWinnerrrr(boardCopy, p):
                    board[boardSpot][1] = c
                    drawBoard()
                    return
    #If code has progressed this far, simply chose a random empty space
    randomMove = True
    while randomMove:
        boardSpot = randint(0,8)
        if board[boardSpot][1] != p and board[boardSpot][1] != c:
            board[boardSpot][1] = c
            randomMove = False
            drawBoard()
#Check if someone has won
def checkWinner(brd, lttr):
    return ((brd[6][1] == lttr and brd[7][1] == lttr and brd[8][1] == lttr) or # across bottom
     (brd[3][1] == lttr and brd[4][1] == lttr and brd[5][1] == lttr) or # across middle
     (brd[0][1] == lttr and brd[1][1] == lttr and brd[2][1] == lttr) or # across top
     (brd[6][1] == lttr and brd[3][1] == lttr and brd[0][1] == lttr) or # down left side
     (brd[7][1] == lttr and brd[4][1] == lttr and brd[1][1] == lttr) or # down middle
     (brd[8][1] == lttr and brd[5][1] == lttr and brd[2][1] == lttr) or # down right side
     (brd[6][1] == lttr and brd[4][1] == lttr and brd[2][1] == lttr) or # diagonal
    (brd[8][1] == lttr and brd[4][1] == lttr and brd[0][1] == lttr)) # diagonal
def checkWinnerr(brd, lttr):
    return ((brd[6][1] == lttr and brd[7][1] == lttr and brd[8][1] == lttr) or # across bottom
     (brd[3][1] == lttr and brd[4][1] == lttr and brd[5][1] == lttr) or # across middle
     (brd[0][1] == lttr and brd[1][1] == lttr and brd[2][1] == lttr) or # across top
     (brd[6][1] == lttr and brd[3][1] == lttr and brd[0][1] == lttr))  # down left side
     
def checkWinnerrr(brd, lttr):
    return ((brd[7][1] == lttr and brd[4][1] == lttr and brd[1][1] == lttr) or # down middle
     (brd[8][1] == lttr and brd[5][1] == lttr and brd[2][1] == lttr) or # down right side
     (brd[6][1] == lttr and brd[4][1] == lttr and brd[2][1] == lttr) or # diagonal
    (brd[8][1] == lttr and brd[4][1] == lttr and brd[0][1] == lttr)) # diagonal

def checkWinnerrrr(brd, lttr):
    return ((brd[6][1] == lttr and brd[7][1] == lttr and brd[8][1] == lttr) or # across bottom
     (brd[3][1] == lttr and brd[4][1] == lttr and brd[5][1] == lttr) or # across middle
     (brd[0][1] == lttr and brd[1][1] == lttr and brd[2][1] == lttr) or # across top
     (brd[6][1] == lttr and brd[3][1] == lttr and brd[0][1] == lttr) or  # down left side
     (brd[7][1] == lttr and brd[4][1] == lttr and brd[1][1] == lttr) or # down middle
     (brd[8][1] == lttr and brd[5][1] == lttr and brd[2][1] == lttr))  # down right side
def checkWinnerrrrr(brd, lttr):
    return ((brd[6][1] == lttr and brd[4][1] == lttr and brd[2][1] == lttr) or # diagonal
    (brd[8][1] == lttr and brd[4][1] == lttr and brd[0][1] == lttr)) # diagonal
#Check for tie
def checkTie(brd):
    emptySpaces = 0
    #Loop through all the board spaces.  If the board space is not X or O, then it is free.
    for x in brd:
        if x[1] != c and x[1] != p:
            emptySpaces += 1
    #If there are 0 empty spaces, prompt user to play again or to quit the game
    if emptySpaces == 0:
        print("The board is full!  You have tied! \n")
        endOfGame()
        return 0
#Either maint a new game or quit the program depending on player input        
def endOfGame():
    response = input("Would you like to play again? Y/N \n")
    if response == "Y" or response == "y":
        
        print("Starting new game...")
        sleep(2)
        main()
    elif response == "N" or response == "n":
        print("Thanks for playing!")
        return
 
    else:
        print("You did not input a valid response!")
        endofGame()

if __name__ == "__main__":
    print("wwelcome to tic tac toe")
    print("select one mode")
    print("1 easy 2 moderate 3 difficult")
    global n
    n=int(input())
    if(n==1):
        main()
    elif(n==2):
        main()
    elif(n==3):
        main()
