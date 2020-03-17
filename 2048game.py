# ------------------------------------------------------------------------------------------------------------- IMPORT -
import random
import time
import os
from copy import deepcopy

# ======================================================================================================== BOARD SETUP =
boardSize = 4

manualSetup = False
board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

points = 0
# -------------------------------------------------------------------------------------------------------- PRINT BOARD -
def printBoard():
    result = ""
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            if board[i][j] == 0:
                result += ".\t"
            else:
                result += str(board[i][j]) + "\t"
        result += "\n\n\n"
    print(result)

# ------------------------------------------------------------------------------------------------- ROW COLLAPSE RIGHT -
def rowCollapseRight(row):
    global points
    # COMPRESS to the right by creating a new row with the numbers right next to each other
    newRow = []
    zeros = 0
    for j in range(len(board) - 1, -1, -1):
        if board[row][j] == 0:
            zeros += 1
        else:
            newRow.insert(0, board[row][j])
    # Adds space to the left from holes
    for i in range(0, zeros):
        newRow.insert(0, 0)
    # Inserts the new compressed row into the board
    for j in range(0, len(board)):
        board[row][j] = newRow[j]
    # MERGE tiles with same numbers from right to left
    for j in range(len(board) - 1, 0, -1):
        if board[row][j] == board[row][j - 1]:
            board[row][j] *= 2
            points += board[row][j] # adds points
            board[row][j - 1] = 0
    # COMPRESS again ..
    newRow = []
    zeros = 0
    for j in range(len(board) - 1, -1, -1):
        if board[row][j] == 0:
            zeros += 1
        else:
            newRow.insert(0, board[row][j])
    for i in range(0, zeros):
        newRow.insert(0, 0)
    for j in range(0, len(board)):
        board[row][j] = newRow[j]

# -------------------------------------------------------------------------------------------------- ROW COLLAPSE LEFT -
def rowCollapseLeft(row):
    global points
    # COMPRESS to the left by creating a new row with the numbers right next to each other
    newRow = []
    zeros = 0
    for j in range(0, len(board)):
        if board[row][j] == 0:
            zeros += 1
        else:
            newRow.insert(len(board) - 1, board[row][j])
    # Adds space to the right from holes
    for j in range(0, zeros):
        newRow.insert(len(board) - 1, 0)
    # Inserts the new compressed row into the board
    for j in range(0, len(board)):
        board[row][j] = newRow[j]
    # MERGE tiles with same numbers from left to right
    for j in range(0, len(board)-1):
        if board[row][j] == board[row][j + 1]:
            board[row][j] *= 2
            points += board[row][j] # adds points
            board[row][j + 1] = 0
    # COMPRESS again ..
    newRow = []
    zeros = 0
    for j in range(0, len(board)):
        if board[row][j] == 0:
            zeros += 1
        else:
            newRow.insert(len(board) - 1, board[row][j])
    for j in range(0, zeros):
        newRow.insert(len(board) - 1, 0)
    for j in range(0, len(board)):
        board[row][j] = newRow[j]

# ------------------------------------------------------------------------------------------------- COLUMN COLLAPSE UP -
def columnCollapseUp(column):
    global points
    # COMPRESS to the top by creating a new column with the numbers right on top of each other
    newColumn = []
    zeros = 0
    for i in range(0, len(board)):
        if board[i][column] == 0:
            zeros += 1
        else:
            newColumn.insert(len(board) - 1, board[i][column])
    # Adds space to the bottom from holes
    for i in range(0, zeros):
        newColumn.insert(len(board) - 1, 0)
    # Inserts the new compressed column into the board
    for i in range(0, len(board)):
        board[i][column] = newColumn[i]
    # MERGE tiles with same numbers from top to bottom
    for i in range(0, len(board) - 1):
        if board[i][column] == board[i + 1][column]:
            board[i][column] *= 2
            points += board[i][column] # adds points
            board[i + 1][column] = 0
    # COMPRESS again ..
    newColumn = []
    zeros = 0
    for i in range(0, len(board)):
        if board[i][column] == 0:
            zeros += 1
        else:
            newColumn.insert(len(board) - 1, board[i][column])
    for i in range(0, zeros):
        newColumn.insert(len(board) - 1, 0)
    for i in range(0, len(board)):
        board[i][column] = newColumn[i]

# ----------------------------------------------------------------------------------------------- COLUMN COLLAPSE DOWN -
def columnCollapseDown(column):
    global points
    # COMPRESS to the bottom by creating a new column with the numbers right on top of each other
    newColumn = []
    zeros = 0
    for i in range(len(board) - 1, -1, -1):
        if board[i][column] == 0:
            zeros += 1
        else:
            newColumn.insert(0, board[i][column])
    # Adds space to the top from holes
    for i in range(0, zeros):
        newColumn.insert(0, 0)
    # Inserts the new compressed column into the board
    for i in range(0, len(board)):
        board[i][column] = newColumn[i]

    # MERGE tiles with same numbers from bottom to top
    for i in range(len(board) - 1, 0, -1):
        if board[i][column] == board[i - 1][column]:
            board[i][column] *= 2
            points += board[i][column] # adds points
            board[i - 1][column] = 0

    # COMPRESS again ..
    newColumn = []
    zeros = 0
    for i in range(len(board) - 1, -1, -1):
        if board[i][column] == 0:
            zeros += 1
        else:
            newColumn.insert(0, board[i][column])
    for i in range(0, zeros):
        newColumn.insert(0, 0)
    for i in range(0, len(board)):
        board[i][column] = newColumn[i]
# ---------------------------------------------------------------------------------------------------- ADD RANDOM TILE -
def addRandomTile():
    # Finds a random empty field on the board and adds either a 2 or a 4
    while True:
        probability = random.uniform(0,1)
        i = random.randint(0,len(board)-1)
        j = random.randint(0,len(board)-1)
        if board[i][j] == 0:
            if probability > 0.1: board[i][j] = 2
            else: board[i][j] = 4
            return
        else:
            continue

# ----------------------------------------------------------------------------------------------------------- NEW GAME -
def newGame():
    # If the setting is not on manual setup it creates a new empty board with the given board size
    if not manualSetup:
        board.clear()
        for i in range(0,boardSize):
            row = []
            for j in range(0,boardSize):
                row.append(0)
            board.append(row)
        addRandomTile()

# -------------------------------------------------------------------------------------------------------------- RIGHT -
def right():
    oldboard = deepcopy(board)
    for r in range(0, len(board)):
        rowCollapseRight(r)
    if oldboard != board:
        addRandomTile()

# --------------------------------------------------------------------------------------------------------------- LEFT -
def left():
    oldboard = deepcopy(board)
    for r in range(0, len(board)):
        rowCollapseLeft(r)
    if oldboard != board:
        addRandomTile()

# ----------------------------------------------------------------------------------------------------------------- UP -
def up():
    oldboard = deepcopy(board)
    for c in range(0, len(board)):
        columnCollapseUp(c)
    if oldboard != board:
        addRandomTile()

# --------------------------------------------------------------------------------------------------------------- DOWN -
def down():
    oldboard = deepcopy(board)
    for c in range(0, len(board)):
        columnCollapseDown(c)
    if oldboard != board:
        addRandomTile()

# ------------------------------------------------------------------------------------------------------------ EXECUTE -

newGame()

while True:
    time.sleep(0.5)
    os.system('cls')
    left()
    printBoard()
    print(points)

    time.sleep(0.5)
    os.system('cls')
    up()
    printBoard()
    print(points)

    time.sleep(0.5)
    os.system('cls')
    right()
    printBoard()
    print(points)

    time.sleep(0.5)
    os.system('cls')
    down()
    printBoard()
    print(points)
