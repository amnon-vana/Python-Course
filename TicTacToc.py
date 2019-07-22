import random

def SetMatrixSize():
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

def ResetMatrix():
    # Reset all cells in matrix to '_'
    for i in range(size):
        for j in range(size):
            matrix[i][j] = '_'

def PrintMatrix():
    # Display matrix status
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=' ')
        print("")

def ChooseFirstPlayerType():
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


def ChooseSecondPlayerType():
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

def AllCellsUsed():
    # Return True if all cells in use else return False
    if used_cell == max_moves:
        return True
    return False

def GameOverDeuce():
    print("########################")
    print("Game over: Deuce")
    print("########################")

def GameOverWin():
    print("########################")
    print("Game over: player {} win".format(player))
    print("########################")
    PrintMatrix()
    print("########################")

def SetPlayerType():
    # Return player type according even or odd movements
    if used_cell % 2 == 0:
        return player1_type
    else:
        return player2_type

def SetPlayer():
    # Return player according even or odd movements
    if used_cell % 2 == 0:
       return player1
    else:
       return player2

def CheckRowWinPossibility():
    # Check if human player has win possibility by row
    # Check every row if missing one sign for full row
    # if possibility exist display message to user
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

def CheckColWinPossibility():
    # Check if human player has win possibility by column
    # Check every column if missing one sign for full column
    # if possibility exist display message to user
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

def CheckLeftDiagWinPossibility():
    # Check if human player has win possibility by left diagonal
    # Check if left diagonal missing one sign for full diagonal
    # if possibility exist display message to user
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

def CheckRightDiagWinPossibility():
    # Check if human player has win possibility by right diagonal
    # Check if right diagonal missing one sign for full diagonal
    # if possibility exist display message to user
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

def CheckDiagWinPossibility():
    CheckLeftDiagWinPossibility()
    CheckRightDiagWinPossibility()

def CheckWinPossibility():
    CheckRowWinPossibility()
    CheckColWinPossibility()
    CheckDiagWinPossibility()

def GetRowFromUser():
    # Get number of row from user until it will be legal input(integer)
    while True:
        answer = input("Enter row number: ")
        if answer.isdigit():
            return int(answer)

def GetRowFromComp():
    # Get random number of row until it will be row with at least one empty cell
    while True:
        x = random.randint(0,size -1)
        for y in range(size):
            if matrix[x][y] == '_':
                return x

def GetColFromUser():
    # Get number of column from user until it will be legal input(integer)
    while True:
        answer = input("Enter column number: ")
        if answer.isdigit():
            return int(answer)

def GetColFromComp():
    # Get random number of column until it will be empty cell
    y = random.randint(0,size - 1)
    while matrix[row][y] != '_':
        y = random.randint(0, size - 1)
    return y

def GetRow():
    if player_type == 'h':
        return GetRowFromUser()
    else:
        return GetRowFromComp()

def GetCol():
    if player_type == 'h':
        return GetColFromUser()
    else:
        return GetColFromComp()

def CellInRange():
    # Return True if cell is in range else return False
    if row in range(size) and col in range(size):
        return True
    return False

def CellIsEmpty():
    # Return True if cell is empty else return False

    if matrix[row][col] == '_':
        return True
    return False

def RowIsFull():
    # Return True if row is full else return False
    retcode = True
    for i in range(size):
        if matrix[row][i] != player:
            retcode = False
            break
    return retcode

def ColIsFull():
    # Return True if column is full else return False
    retcode = True
    for i in range(size):
        if matrix[i][col] != player:
            retcode = False
            break
    return retcode

def LeftDiagIsFull():
    # Return True if left diagonal is full else return False
    retcode = True
    for i in range(size):
        if matrix[i][i] != player:
            retcode = False
            break
    return retcode

def RightDiagIsFull():
    # Return True if right diagonal is full else return False
    retcode = True
    for i in range(size):
        if matrix[i][size - 1 - i] != player:
            retcode = False
            break
    return retcode

def DiagIsFull():
    # Return True if one diagonal at least is full else return False
    if row == col:
        if size % 2 == 1:
            return LeftDiagIsFull() or RightDiagIsFull()
        else:
            return LeftDiagIsFull()
    elif row + col + 1 == size:
        return RightDiagIsFull()
    else:
        return False

def PlayerWinTheGame():
    # Return True if player win the game else return False
    if RowIsFull() or ColIsFull() or DiagIsFull():
        return True
    return False

def PlayAgain():
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

size = SetMatrixSize()
matrix = [[0] * size for i in range(size)]
max_moves = size ** 2

while want_to_play:
    player1_type = ChooseFirstPlayerType()
    player2_type = ChooseSecondPlayerType()
    ResetMatrix()
    used_cell = 0
    while True:
        PrintMatrix()
        if AllCellsUsed():
            GameOverDeuce()
            want_to_play = AnotherGame()
            break
        player = SetPlayer()
        player_type = SetPlayerType()
        print("Player {} is playing now.".format(player))
        if size * 2 - 2 <= used_cell and player_type == 'h':
            CheckWinPossibility()
        row = GetRow()
        col = GetCol()
        if CellInRange():
            if CellIsEmpty():
                matrix[row][col] = player
                used_cell += 1
                if size * 2 - 1 <= used_cell and PlayerWinTheGame():
                    GameOverWin()
                    want_to_play = PlayAgain()
                    break
            else:
                print("Cell not empty try another cell")
        else:
            print("Cell not in range try again")
