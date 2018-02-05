width, height = 7, 6
board = [[0 for x in range(width)] for y in range(height)]
myTurn, oppTurn = 1, 2

def main():
    printBoard(board)
    conectatec(2, board)
    printBoard(board)


def conectatec(turn, _board):
    board = _board
    global myTurn, oppTurn
    if turn == 1:
        myTurn = 1
        oppTurn = 2
    else:
        myTurn = 2
        oppTurn = 1

    score = -999999999
    move = None

    moves = {}
    for i in range(width):
        if canBePlacedIn(i, board):
            temp = place(i, board, myTurn)
            #printBoard(temp)
            moves[i] = minimax(temp)
            #print (moves[i])

    for possible_move, partial_score in moves.items():
        #print ("----> p_score:", partial_score)
        if partial_score >= score:
            score = partial_score
            move = possible_move
    print("tiro en la columna ",move)
    return move

def canBePlacedIn(column, _board):
    for i in range(height):
        if _board[i][column] == 0:
            return True
    return False

def place(column, _board, turn):
    possibleMove = [x[:] for x in _board]
    if(column >= width or column < 0):
        return -1
    row = height - 1
    while(row >= 0 and possibleMove[row][column] == 0):
        row -= 1
    possibleMove[row+1][column] = turn
    return possibleMove

def minimax(_board):
    score = 99999999
    for i in range(width):
        if canBePlacedIn(i, _board):
            #moves[i] = max(place(i, oppTurn))
            temp = place(i, _board, oppTurn)
            score = min(score, heuristicScore(temp))
            #print ("----------------", score)
            #printBoard(temp)
    return score

def heuristicScore(_board):
    score = 1000

    for i in range(height):
        for j in range(width):
            
            #Heuristic1
            if _board[i][j] == myTurn:
                score = score - abs(i - width/2) - abs(j - height/2)

            #Heuristic2
            if _board[i][j] == myTurn:
                score += checkNearby(i, j, _board, myTurn)
            elif _board[i][j] == oppTurn:
                score -= checkNearby(i, j, _board, oppTurn)

            #Heuristic3
            if _board[i][j] == myTurn:
                score += checkT(i, j, _board, myTurn)+1
            elif _board[i][j] == oppTurn:
                score -= checkT(i, j, _board, oppTurn)
    return score

def checkNearby(row, col, _board, turn):
    score = 1

    # Check for pieces around
    if (row < height-1 and _board[row + 1][col] == turn):
        score += 200
    if (row < height-1 and col < width-1 and _board[row + 1][col + 1] == turn):
        score += 300
    if (col < width-1 and _board[row][col + 1] == turn):
        score += 400
    if (row > 0 and col < width-1 and _board[row - 1][col + 1] == turn):
        score += 600
    if (row > 0 and _board[row - 1][col] == turn):
        score += 400
    if (row > 0 and col > 0 and _board[row - 1][col - 1] == turn):
        score += 300
    if (col > 0 and _board[row][col - 1] == turn):
        score += 400
    if (row < height-1 and col > 0 and _board[row + 1][col - 1] == turn):
        score += 200

    return score

def checkT(row, col, _board, turn):
    score = 0
    found = False

    # Check for 3-in-a-row horizontal, vertical or diagonal
    if (0 < col < width-1 and row < height-1 and _board[row + 1][col - 1] == turn and _board[row + 1][col] == turn and _board[row + 1][col + 1] == turn):
        score += 10000
        found = True
    if (0 < row < height-1 and col < width-1 and _board[row - 1][col + 1] == turn and _board[row][col + 1] == turn and _board[row + 1][col + 1] == turn and row > 0):
        score += 10000
        found = True
    if (0 < col < width-1 and row > 0 and _board[row - 1][col - 1] == turn and _board[row - 1][col] == turn and _board[row - 1][col + 1] == turn):
        score += 10000
        found = True
    if (0 < row < height-1 and col > 0 and _board[row - 1][col - 1] == turn and _board[row][col - 1] == turn and _board[row + 1][col - 1] == turn):
        score += 10000
        found = True
    if (row < height-2 and col < width-2 and _board[row + 2][col] == turn and _board[row + 1][col + 1] == turn and _board[row][col + 2] == turn):
        score += 10000
        found = True
    if (row > 1 and col < width-2 and _board[row][col + 2] == turn and _board[row - 1][col + 1] == turn and _board[row - 2][col] == turn):
        score += 10000
        found = True
    if (row > 1 and col > 1 and _board[row - 2][col] == turn and _board[row - 1][col - 1] == turn and _board[row][col - 2] == turn):
        score += 10000
        found = True
    if (row < height-2 and col > 1 and _board[row][col - 2] == turn and _board[row + 1][col - 1] == turn and _board[row + 2][col] == turn):
        score += 10000
        found = True

    # Check for L's
    if (row < height-2 and col > 0 and _board[row + 1][col] == turn and _board[row + 2][col] == turn and _board[row + 1][col - 1] == turn):
        score += 10000
        found = True
    if (row < height-2 and col < width-1 and _board[row + 1][col] == turn and _board[row + 2][col] == turn and _board[row + 1][col + 1] == turn):
        score += 10000
        found = True
    if (row < height-1 and col < width-2 and _board[row][col + 1] == turn and _board[row][col + 2] == turn and _board[row + 1][col + 1] == turn):
        score += 10000
        found = True
    if (row > 0 and col < width-2 and _board[row][col + 1] == turn and _board[row][col + 2] == turn and _board[row - 1][col + 1] == turn):
        score += 10000
        found = True
    if (row > 1 and col > 0 and _board[row - 1][col] == turn and _board[row - 2][col] == turn and _board[row - 1][col - 1] == turn):
        score += 10000
        found = True
    if (row > 1 and col < width-1 and _board[row - 1][col] == turn and _board[row - 2][col] == turn and _board[row - 1][col + 1] == turn):
        score += 10000
        found = True
    if (row < height-1 and col > 1 and _board[row][col - 1] == turn and _board[row][col - 2] == turn and _board[row + 1][col - 1] == turn):
        score += 10000
        found = True
    if (row > 0 and col > 1 and _board[row][col - 1] == turn and _board[row][col - 2] == turn and _board[row - 1][col - 1] == turn):
        score += 10000
        found = True

    if (found and turn == myTurn):
        score *= 100

    return score



def printBoard(_board):
    for x in range(height-1,-1, -1):
        for y in range(width):
            print (_board[x][y], end = '')
        print ("\n")
    print ("\n")

if __name__ == '__main__':
    main()

