# Simple Minimax implementation for Tic-Tac-Toe game
import math

# Function to check if any player has won the game
def check_winner(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
                      (0, 4, 8), (2, 4, 6)]            # diagonals
                      
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != ' ':
            return board[condition[0]]
    return None

# Function to check if the game is a draw2
def is_draw(board):
    return ' ' not in board

# Minimax function
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    # Assign scores: +1 for maximizing player win, -1 for minimizing player win, 0 for draw
    if winner == 'X':  # X is the maximizing player
        return 1
    elif winner == 'O':  # O is the minimizing player
        return -1
    elif is_draw(board):
        return 0
    
    # Maximizing player's move (X)
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '  # Undo the move
                best_score = max(score, best_score)
        return best_score

    # Minimizing player's move (O)
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '  # Undo the move
                best_score = min(score, best_score)
        return best_score

# Function to find the best move for the current player
def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'  # Assuming the AI plays as 'X'
            score = minimax(board, 0, False)
            board[i] = ' '  # Undo the move
            if score > best_score:
                best_score = score
                move = i
    return move

# Function to print the board
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('|'.join(row))
        print('-'*5)

# Example: Play Tic-Tac-Toe game
def play_game():
    board = [' '] * 9
    current_player = 'X'  # Let's assume AI is 'X' and human is 'O'
    
    while True:
        print_board(board)
        
        if check_winner(board) or is_draw(board):
            break
        
        if current_player == 'X':  # AI's turn
            print("AI's Move")
            move = best_move(board)
            board[move] = 'X'
        else:  # Human's turn
            move = int(input("Enter your move (0-8): "))
            if board[move] == ' ':
                board[move] = 'O'
            else:
                print("Invalid move! Try again.")
                continue
        
        current_player = 'O' if current_player == 'X' else 'X'
    
    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a draw!")

# Run the game
play_game()
