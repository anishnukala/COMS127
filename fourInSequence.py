#fourInSequence.py
# Anish Reddy Nukala           01-04-2024
# Assignment 4
# Description: The "Four In Sequence" , This game has 2 players and has 3 features like Play, instructions and quit , in game we have developed code to function , in instructions we have developed the instructions of the game , while clicking on the quit button the game is going to end.
import random
import sys

def printTitleMaterial():
    print("Four In Sequence!")
    print()
    print("By: Anish Reddy Nukala")
    print("[COM S 127 B]")
    print()

def initialChoice():
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

def chooseNumPlayers():
    numPlayers = int(input("Number of Players? [1] / [2]: "))
    while numPlayers != 1 and numPlayers != 2:
        print("ERROR: Please enter either 1 or 2...")
        numPlayers = int(input("Number of Players? [1] / [2]: "))
    return numPlayers

def printBanner():
    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()

def getPlayerPiece(playerNumber):
    piece = ""
    if playerNumber == 0:
        piece = "."
    elif playerNumber == 1:
        piece = "X"
    elif playerNumber == 2:
        piece = "O"
    return piece

def createBoard(width, height):
    empty = getPlayerPiece(0)
    board = []
    for i in range(0, height):
        board.append([])
        for j in range(0, width):
            board[i].append(empty)
    return board

def printBoard(board):
    for row in board:
        for column in row:
            print(column, end="")
        print()
    for i in range(0, len(board[0])):
        print(i, end="")
    print()
    print()

def getColumnInt(board, playerNumber):
    return int(input("Player {0}, please select a column between (0-{1}): ".format(playerNumber, len(board[0]) - 1)))

def getInputInRange(board, playerNumber):
    col = getColumnInt(board, playerNumber)
    while col < 0 or col > len(board[0]) - 1:
        print("ERROR: Value must be between (0-{0}). You entered: {1}".format(len(board[0]) - 1, col))
        col = getColumnInt(board, playerNumber)
    return col

def getHumanInput(board, playerNumber):
    col = getInputInRange(board, playerNumber)
    while getOpenRow(board, col) == -1:
        print("ERROR: Column {0} is full! Please choose a different column...".format(col))
        col = getInputInRange(board, playerNumber)
    return col

def checkForNextMoveWin(board, playerNumber):
    empty = getPlayerPiece(0)
    piece = getPlayerPiece(playerNumber)

    for col in range(len(board[0])):
        row = getOpenRow(board, col)
        if row != -1:
            board[row][col] = piece
            if checkWinner(board, playerNumber):
                board[row][col] = empty
                return col
            board[row][col] = empty

    return -1

def checkAdjacent(board, playerNumber):
    col = -1
    piece = getPlayerPiece(playerNumber)
    adjacents = []

    for column in range(0, len(board[0])):
        row = getOpenRow(board, column)
        if row != -1:
            if row - 1 >= 0 and column - 1 >= 0:
                if board[row-1][column-1] == piece:
                    adjacents.append(column)

            if column - 1 >= 0:
                if board[row][column-1] == piece:
                    adjacents.append(column)

            if row + 1 < len(board) and column - 1 >= 0:
                if board[row+1][column-1] == piece:
                    adjacents.append(column)

            if row + 1 < len(board):
                if board[row+1][column] == piece:
                    adjacents.append(column)

            if row - 1 >= 0 and column + 1 < len(board[0]):
                if board[row-1][column+1] == piece:
                    adjacents.append(column)

            if column + 1 < len(board[0]):
                if board[row][column+1] == piece:
                    adjacents.append(column)

            if row + 1 < len(board) and column + 1 < len(board[0]):
                if board[row+1][column+1] == piece:
                    adjacents.append(column)

    if len(adjacents) > 0:
        col = random.choice(adjacents)

    return col

def getComputerInput(board, playerNumber):
    col = checkForNextMoveWin(board, playerNumber)
    if col == -1:
        col = checkForNextMoveWin(board, playerNumber % 2 + 1)
        if col == 1:
            col = checkAdjacent(board, playerNumber)
            if col == 1:
                col = random.randint(0, len(board[0]) - 1)
                while getOpenRow(board, col) == -1:
                    col = random.randint(0, len(board[0]) - 1)
    return col

def getOpenRow(board, col):
    for row in range(len(board)-1, -1, -1):
        if board[row][col] == getPlayerPiece(0):
            return row
    return -1

def checkWinner(board, playerNumber):
    piece = getPlayerPiece(playerNumber)

    for row in range(0, len(board)):
        for column in range(0, len(board[0]) - 3):
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
                return True

    for row in range(0, len(board) - 3):
        for column in range(0, len(board[0])):
            if board[row][column] == piece and board[row+1][column] == piece and board[row+2][column] == piece and board[row+3][column] == piece:
                return True

    for row in range(0, len(board) - 3):
        for column in range(0, len(board[0]) - 3):
            if board[row][column] == piece and board[row+1][column+1] == piece and board[row+2][column+2] == piece and board[row+3][column+3] == piece:
                return True

    for row in range(3, len(board)):
        for column in range(0, len(board[0]) - 3):
            if board[row][column] == piece and board[row-1][column+1] == piece and board[row-2][column+2] == piece and board[row-3][column+3] == piece:
                return True

    return False

def playGame(numPlayers):
    width = 7
    height = 6
    board = createBoard(width, height)

    playerNumber = 1
    moves = 0

    while True:
        printBoard(board)

        if numPlayers == 1 and playerNumber == 2:
            col = getComputerInput(board, playerNumber)
        else:
            col = getHumanInput(board, playerNumber)

        row = getOpenRow(board, col)
        board[row][col] = getPlayerPiece(playerNumber)

        if checkWinner(board, playerNumber):
            printBoard(board)
            print("Player {0} wins!".format(playerNumber))
            break

        moves += 1
        if moves == width * height:
            printBoard(board)
            print("It's a tie!")
            break

        playerNumber = 3 - playerNumber

def printInstructions():
    print("Welcome to Four In Sequence!")
    print()
    print("The goal of the game is to get four of your pieces in a row, either horizontally, vertically, or diagonally.")
    print("Players take turns placing their pieces in one of the seven columns.")
    print("The piece will then fall to the lowest available spot in that column.")
    print("The game ends when one player connects four pieces or when the board is full and the game is a tie.")
    print()

def main():
    printTitleMaterial()

    choice = initialChoice()

    while choice != "q":
        if choice == "p":
            numPlayers = chooseNumPlayers()
            playGame(numPlayers)
        elif choice == "i":
            printInstructions()

        choice = initialChoice()

    print("Goodbye!")

if __name__ == "__main__":
    main()
