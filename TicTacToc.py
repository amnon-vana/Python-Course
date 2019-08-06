import random

def setMatrixSize():
    '''
    get matrix size from user
    :return: matrix size
    '''
    answer = 0
    while answer < 3 or answer >10:
        answer = input("Enter matrix size between (3-10): ")
        if answer.isdigit():
            answer = int(answer)
        else:
            answer = 0
    return answer

def resetMatrix():
    # Reset all cells in matrix to '_'
    for i in range(size):
        for j in range(size):
            matrix[i][j] = '_'

def printMatrix():
    # Display matrix status
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=' ')
        print("")

def chooseFirstPlayerType():
    '''
    Get first user type from user:
    h for human
    c for computer
    :return: user type
    '''
    answer = None
    while answer not in ['h', 'c']:
        answer = (input("Choose first player (H - for human or C - for computer): ")).lower()
    return answer


def chooseSecondPlayerType():
    '''
    Get second user type from user:
    h for human
    c for computer
    :return: user type
    '''
    answer = None
    array = ['h', 'c']
    while answer not in array:
        answer = (input("Choose second player (H - for human or C - for computer): ")).lower()
    return answer.lower()

def allCellsUsed(used_cell):
    # Return True if all cells in use else return False
    if used_cell == max_moves:
        return True
    return False

def gameOverDeuce():
    print("########################")
    print("Game over: Deuce")
    print("########################")

def gameOverWin():
    print("########################")
    print("Game over: player {} win".format(player))
    print("########################")
    printMatrix()
    print("########################")

def setPlayerType():
    # Return player type according even or odd movements
    if used_cell % 2 == 0:
        return player1_type
    else:
        return player2_type

def setPlayer():
    # Return player according even or odd movements
    if used_cell % 2 == 0:
       return player1
    else:
       return player2

def checkRowWinPossibility(matrix,size):
    '''
        :param matrix: matrix status
        :param size: matrix size
        :return:nothing
        Check if human player has win possibility by row
        Check every row if missing one sign for full row
        if possibility exist display message to user
    '''
    for i in range(size):
        count = 0
        free_cell = ''
        for j in range(size):
            if matrix[i][j] == player:
                count += 1
            elif matrix[i][j] == '_':
                free_cell = str(i) + "," + str(j)
            else:
                break
        if count + 1 == size:
            print("Matchpoint at cell: {}".format(free_cell))

def checkColWinPossibility(matrix,size):
    '''
        :param matrix: matrix status
        :param size: matrix size
        :return:nothing
        Check if human player has win possibility by column
        Check every column if missing one sign for full column
        if possibility exist display message to user
    '''
    for i in range(size):
        count = 0
        free_cell = ''
        for j in range(size):
            if matrix[j][i] == player:
                count += 1
            elif matrix[j][i] == '_':
                free_cell = str(j) + "," + str(i)
            else:
                break
        if count + 1 == size:
            print("Matchpoint at cell: {}".format(free_cell))

def checkLeftDiagWinPossibility(matrix,size):
    '''
        :param matrix: matrix status
        :param size: matrix size
        :return:nothing
        Check if human player has win possibility by left diagonal
        Check if left diagonal missing one sign for full diagonal
        if possibility exist display message to user
    '''
    count = 0
    free_cell = ''
    for i in range(size):
        if matrix[i][i] == player:
            count += 1
        elif matrix[i][i] == '_':
            free_cell = str(i) + "," + str(i)
        else:
            break
    if count + 1 == size:
        print("Matchpoint at cell: {}".format(free_cell))

def checkRightDiagWinPossibility(matrix,size):
    '''
        :param matrix: matrix status
        :param size: matrix size
        :return:nothing
        Check if human player has win possibility by right diagonal
        Check if right diagonal missing one sign for full diagonal
        if possibility exist display message to user
    '''
    count = 0
    free_cell = ''
    for i in range(size):
        if matrix[i][size - i - 1] == player:
            count += 1
        elif matrix[i][size - i - 1] == '_':
            free_cell = str(i) + "," + str(i)
        else:
            break
    if count + 1 == size:
        print("Matchpoint at cell: {}".format(free_cell))

def checkDiagWinPossibility(matrix,size):
    checkLeftDiagWinPossibility(matrix,size)
    checkRightDiagWinPossibility(matrix,size)

def checkWinPossibility(matrix,size):
    checkRowWinPossibility(matrix,size)
    checkColWinPossibility(matrix,size)
    checkDiagWinPossibility(matrix,size)

def getRowFromUser():
    '''
        Get row number from user until it will be legal input(integer)
        :return: row number

    '''
    while True:
        answer = input("Enter row number: ")
        if answer.isdigit():
            return int(answer)

def getRowFromComp():
    '''
        Get random number of row until it will be row with at least one empty cell
        :return: row number
    '''
    while True:
        x = random.randint(0,size -1)
        for y in range(size):
            if matrix[x][y] == '_':
                return x

def getColFromUser():
    '''
         Get number of column from user until it will be legal input(integer)
         :return: col number
     '''
    while True:
        answer = input("Enter column number: ")
        if answer.isdigit():
            return int(answer)

def getColFromComp():
    '''
        Get random number of column until it will be empty cell
        :return: row number
    '''
    y = random.randint(0,size - 1)
    while matrix[row][y] != '_':
        y = random.randint(0, size - 1)
    return y

def getRow():
    if player_type == 'h':
        return getRowFromUser()
    else:
        return getRowFromComp()

def getCol():
    if player_type == 'h':
        return getColFromUser()
    else:
        return getColFromComp()

def cellInRange(size):
    '''
    Return True if cell is in range else return Fals
    :param size:
    :return: True / False
    '''
    if row in range(size) and col in range(size):
        return True
    return False

def cellIsEmpty(row,col):
    '''
    Return True if cell is empty else return False
    :param row: row number
    :param col: column number
    :return: True / False
    '''
    if matrix[row][col] == '_':
        return True
    return False

def rowIsFull(row,size,player,matrix):
    '''
    Return True if row is full else return False
    :param col: column number
    :param size: matrix size
    :param player: player char
    :param matrix: matrix status
    :return: True / False
    '''
    retcode = True
    for i in range(size):
        if matrix[row][i] != player:
            retcode = False
            break
    return retcode

def colIsFull(col,size,player,matrix):
    '''
    Return True if column is full else return False
    :param col: column number
    :param size: matrix size
    :param player: player char
    :param matrix: matrix status
    :return: True / False
    '''
    retcode = True
    for i in range(size):
        if matrix[i][col] != player:
            retcode = False
            break
    return retcode

def leftDiagIsFull(size,player,matrix):
    '''
    Return True if left diagonal is full else return False
    :param size: matrix size
    :param player: player char
    :param matrix: matrix status
    :return: True / False
    '''
    retcode = True
    for i in range(size):
        if matrix[i][i] != player:
            retcode = False
            break
    return retcode

def rightDiagIsFull(size,player,matrix):
    '''
    Return True if right diagonal is full else return False
    :param size: matrix size
    :param player: player char
    :param matrix: matrix status
    :return: True / False
    '''
    retcode = True
    for i in range(size):
        if matrix[i][size - 1 - i] != player:
            retcode = False
            break
    return retcode

def diagIsFull(row,col,size,player,matrix):
    '''
    Return True if one diagonal at least is full else return False
    :param row: row number
    :param col: column number
    :param size: matrix size
    :param player: player char
    :param matrix: matrix status
    :return: True / False
    '''
    if row == col:
        if size % 2 == 1:
            return leftDiagIsFull(size,player,matrix) or rightDiagIsFull(size,player,matrix)
        else:
            return leftDiagIsFull(size,player,matrix)
    elif row + col + 1 == size:
        return rightDiagIsFull(size,player,matrix)
    else:
        return False

def playerWinTheGame(row,col,size,player,matrix):
    # Return True if player win the game else return False
    if rowIsFull(row,size,player,matrix) or colIsFull(col,size,player,matrix) or diagIsFull(row,col,size,player,matrix):
        return True
    return False

def playAgain():
    # Return True if player want to play another game else return False
    answer = None
    while answer not in ['y', 'n']:
        answer = input("Do you want play(y/n): ").lower()
    if answer == 'y':
        return True
    return False


####################
####    Main    ####
####################
player1 = 'x'
player2 = 'o'
want_to_play = True

size = setMatrixSize()
matrix = [[0] * size for i in range(size)]
max_moves = size ** 2

while want_to_play:
    player1_type = chooseFirstPlayerType()
    player2_type = chooseSecondPlayerType()
    resetMatrix()
    used_cell = 0
    while True:
        printMatrix()
        if allCellsUsed(used_cell):
            gameOverDeuce()
            want_to_play = playAgain()
            break
        player = setPlayer()
        player_type = setPlayerType()
        print("Player {} is playing now.".format(player))
        # Check for win possibility only for human player and player has minimum moves to win
        if size * 2 - 2 <= used_cell and player_type == 'h':
            checkWinPossibility(matrix,size)
        row = getRow()
        col = getCol()
        if cellInRange(size):
            if cellIsEmpty(row,col):
                matrix[row][col] = player
                used_cell += 1
                if size * 2 - 1 <= used_cell and playerWinTheGame(row,col,size,player,matrix):
                    gameOverWin()
                    want_to_play = playAgain()
                    break
            else:
                print("Cell not empty try another cell")
        else:
            print("Cell not in range try again")





