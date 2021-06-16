import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                count+=1
    if count%2==0:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                possible_moves.add((i,j))

    return possible_moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]
    move = player(board)
    for i in range(3):
        for j in range(3):
            if (i, j) == action and board[i][j] == EMPTY:
                new_board[i][j] = move
            elif (i,j)==action:
                raise ValueError
            else:
                new_board[i][j] = board[i][j]
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    I sincerely apologize for the lazy implementation.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != EMPTY:
            if board[i][0] == "X":
                return X
            else:
                return O

    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != EMPTY:
            if board[0][i] == "X":
                return X
            else:
                return O

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        if board[0][0] == "X":
            return X
        else:
            return O

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        if board[0][2] == "X":
            return X
        else:
            return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    over = True
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                over = False

    return over or winner(board) is not None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if not terminal(board):
        raise ValueError

    playa = winner(board)
    if playa == X:
        return 1
    elif playa == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def maxplayer(board):
        # Maximize
        if terminal(board):
            return None, utility(board)
        max_score = -2
        best_move = ()
        possible_moves = actions(board)
        for move in possible_moves:
            after_move_board = result(board,move)
            score = minplayer(after_move_board)[1]
            if score > max_score:
                max_score = score
                best_move = move
            if score == 1:
                break
        return best_move, max_score

    def minplayer(board):
        # Minimize
        if terminal(board):
            return None, utility(board)
        min_score = 2
        best_move = ()
        possible_moves = actions(board)
        for move in possible_moves:
            after_move_board = result(board,move)
            score = maxplayer(after_move_board)[1]
            if score<min_score:
                min_score = score
                best_move = move
            if score == -1:
                break
        return best_move, min_score

    if player(board) == X:
        return maxplayer(board)[0]
    else:
        return minplayer(board)[0]
