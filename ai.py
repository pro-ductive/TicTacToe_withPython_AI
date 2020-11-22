def checkBoard(board):
    for i in board:
        if i == ".":
            return True
        else:
            pass
    return False
def checkWin(board, who):
    s1 = [0, 1, 2]
    s2 = [3, 4, 5]
    s3 = [6, 7, 8]
    s4 = [0, 3, 6]
    s5 = [1, 4, 7]
    s6 = [2, 5, 8]
    s7 = [0, 4, 8]
    s8 = [2, 4, 6]
    vals = [s1, s2, s3, s4, s5, s6, s7, s8]
    for i in vals:
        if board[i[0]] == who and board[i[1]] == who and board[i[2]] == who:
            return True
        else:
            pass
    return False
def aiBot(board):
    bestscore=-9
    bestmove=-1
    for i in range(9):
        if board[i]==".":
            board[i]="O"
            score=minimax(board,False)
            board[i]="."
            if score>bestscore:
                bestscore=score
                bestmove=i
    board[bestmove]="O"
def minimax(board,maximizing):
    if checkWin(board,"X"):
        return -1
    elif checkWin(board,"O"):
        return 1
    elif not checkBoard(board):
        return 0
    if maximizing:
        bestscore=-9
        for i in range(9):
            if board[i]==".":
                board[i]="O"
                score=minimax(board,False)
                board[i]="."
                bestscore=max(score,bestscore)
        return bestscore
    else:
        bestscore =9
        for i in range(9):
            if board[i] == ".":
                board[i] = "X"
                score = minimax( board, True)
                board[i] = "."
                bestscore=min(score,bestscore)
        return bestscore