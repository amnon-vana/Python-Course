def checkRowWin(row,sign):
    if matrix[row][0] == sign and matrix[row][1] == sign and matrix[row][2] == sign:
        return True
    return False

def checkColWin(col,sign):
    if matrix[0][col] == sign and matrix[1][col] == sign and matrix[2][col] == sign:
         return True
    return False

def checkFullMatrix():
    for i in matrix:
        if i[0] == '_':
            return False
    return True

#def checkLegalPosition(row,col,sign):



res = checkRowWin(1,"x")
print(f"Result is {res}")

res = checkColWin(1,"x")
print(f"Result is {res}")

