"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    # Count how many Xs and Os are on the board
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    
    # X goes first, so if x_count <= o_count, it's X's turn
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        raise Exception("Action cannot be None")
        
    i, j = action
    if not (0 <= i < 3 and 0 <= j < 3):
        raise Exception("Action coordinates are out of bounds")
        
    if board[i][j] is not EMPTY:
        raise Exception("Cell is already occupied")
        
    # Deep copy the board to avoid modifying the original one
    new_board = deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] is not EMPTY and row[0] == row[1] == row[2]:
            return row[0]
            
    # Check columns
    for col in range(3):
        if board[0][col] is not EMPTY and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
            
    # Check diagonals
    if board[1][1] is not EMPTY:
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
            
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game is over if someone has won
    if winner(board) is not None:
        return True
        
    # Game is over if there are no empty spots left
    for row in board:
        if EMPTY in row:
            return False
            
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    verdict = winner(board)
    if verdict == X:
        return 1
    elif verdict == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
        
    current_player = player(board)
    
    if current_player == X:
        # X is the maximizer
        val, move = max_value(board, float('-inf'), float('inf'))
        return move
    else:
        # O is the minimizer
        val, move = min_value(board, float('-inf'), float('inf'))
        return move


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None
        
    v = float('-inf')
    best_move = None
    
    for action in actions(board):
        val, _ = min_value(result(board, action), alpha, beta)
        if val > v:
            v = val
            best_move = action
        alpha = max(alpha, v)
        if alpha >= beta:
            break
            
    return v, best_move


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None
        
    v = float('inf')
    best_move = None
    
    for action in actions(board):
        val, _ = max_value(result(board, action), alpha, beta)
        if val < v:
            v = val
            best_move = action
        beta = min(beta, v)
        if alpha >= beta:
            break
            
    return v, best_move
