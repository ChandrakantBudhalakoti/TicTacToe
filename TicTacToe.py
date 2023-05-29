import random

# The game board
board = [' ' for _ in range(9)]

# Constants for players and empty spots
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Possible winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]              # diagonals
]


def print_board():
    """Prints the current game board"""
    print("-------------")
    for i in range(3):
        print(f"| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |")
        print("-------------")


def is_winner(board, player):
    """Checks if the specified player has won"""
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False


def is_board_full(board):
    """Checks if the game board is full"""
    return all(cell != EMPTY for cell in board)


def get_empty_cells(board):
    """Returns a list of indices for empty cells"""
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def minimax(board, depth, maximizing_player):
    """Recursive function that implements the Minimax algorithm"""
    if is_winner(board, AI):
        return 1
    elif is_winner(board, HUMAN):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for empty_cell in get_empty_cells(board):
            board[empty_cell] = AI
            eval_score = minimax(board, depth + 1, False)
            board[empty_cell] = EMPTY
            max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for empty_cell in get_empty_cells(board):
            board[empty_cell] = HUMAN
            eval_score = minimax(board, depth + 1, True)
            board[empty_cell] = EMPTY
            min_eval = min(min_eval, eval_score)
        return min_eval


def get_best_move(board):
    """Returns the best possible move for the AI player"""
    best_score = float('-inf')
    best_move = None

    for empty_cell in get_empty_cells(board):
        board[empty_cell] = AI
        score = minimax(board, 0, False)
        board[empty_cell] = EMPTY

        if score > best_score:
            best_score = score
            best_move = empty_cell

    return best_move


def play():
    """Main game loop"""
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Human's turn
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] != EMPTY:
            print("Invalid move. Try again.")
            continue

        board[human_move] = HUMAN
        print_board()

        if is_winner(board, HUMAN):
            print("You win!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        # AI's turn
        print("AI's turn...")
        ai_move = get_best_move(board)
        board[ai_move] = AI
        print_board()

        if is_winner(board, AI):
            print("AI wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break


# Start the game
play()
