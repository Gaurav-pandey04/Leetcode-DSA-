# Function to check is it safe to place queen at board[row][col]
def isSafe(mat, row, col):
    n = len(mat)

    # check this col on upperSide
    for i in range(row):
        if mat[i][col]:
            return False
    
    # check upper diagonal on left side
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if mat[i][j]:
            return False
        
    # check upper diagnoal on right side
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if mat[i][j]:
            return False
        
    return True

def placedQueen(row, mat):
    n = len(mat)
    
    # If all queens are placed return True
    if row == n:
        return True
    
    # consider the row and try placing queen in all columns one by one
    for i in range(n):
        # check if queen can be placed
        if isSafe(mat, row, i):
            mat[row][i] = 1
            if placedQueen(row+1, mat):
                return True
            mat[row][i] = 0

    return False

# Function to find the solution to N-Queens problem
def nQueens(n):
    # Intialise the board
    mat = [[0 for _ in range(n)] for _ in range(n)]

    # If the solution exist
    if placedQueen(0, mat):
        # to store column of the queens
        ans = []
        for i in range(n):
            for j in range(n):
                if mat[i][j]:
                    ans.append(j+1)
        return ans 
    else:
        return [-1]

if __name__=="__main__":
    n = 4
    ans = nQueens(n)
    print(" ".join(map(str, ans)))