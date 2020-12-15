import copy
ENFORCE_ABELIT = False
EMPTY = 'EMPTY'


groups = []


def isFinished(board, n):
    for i in range(0, n):
        for j in range(0, n):
            if (board[i][j] == EMPTY):
                return False
    return True


def isAsosiative(board, n):
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                if(board[int(board[i][j])][k] != board[i][int(board[j][k])]):
                    return False
    return True


def isValid(board, n, right, left, val):
    if (right >= n and left >= n):
        return False
    elif (right >= n and left < n):
        for i in range(0, n):
            if(board[right - 1][i] == val):
                return False
            if(board[i][left] == val):
                return False
    elif (right < n and left >= n):
        for i in range(0, n):
            if(board[right][i] == val):
                return False
            if(board[i][left - 1] == val):
                return False
    else:
        for i in range(0, n):
            if(board[right][i] == val):
                return False
            if(board[i][left] == val):
                return False
    return True


def find_groups_aux(n):
    board = []
    row = []
    for i in range(0, n):
        for j in range(0, n):
            if (i == 0):
                row.append(j)
            else:
                row.append(EMPTY)
        board.append(row)
        board[i][0] = i
        row = []
    return find_groups(board, n, 1, 1)


def find_groups(board, n, row, col):
    cnt = 0
    # print_board(board, n)
    if (row == n and col == n and isFinished(board, n) and isAsosiative(board, n)):
        print_board(board, n)
        return 1
    for i in range(0, n):
        if(isValid(board, n, row, col, i)):
            board[row][col] = i
            if (row < n-1):
                cnt += find_groups(copy.deepcopy(board), n, row + 1, col)
            if (row == n-1 and col < n-1):
                cnt += find_groups(copy.deepcopy(board), n, 1, col + 1)
            if (row == n-1 and col == n-1):
                cnt += find_groups(copy.deepcopy(board), n, row + 1, col + 1)

    return cnt


def print_board(board, n):
    for i in board:
        print('\t'.join(map(str, i)))
    print("===========\n")


print("FOUND:: ", find_groups_aux(2))
