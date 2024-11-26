def winner(b):  # Check for a winner or draw
    for line in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if b[line[0]] == b[line[1]] == b[line[2]] != " ":
            return 10 if b[line[0]] == "X" else -10
    return 0 if " " not in b else None

def minimax(b, turn):  # Minimax algorithm
    result = winner(b)
    if result is not None:
        return result
    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = "X" if turn else "O"
            scores.append(minimax(b, not turn))
            b[i] = " "
    return max(scores) if turn else min(scores)

# Main game logic
board = [" "] * 9
while winner(board) is None:
    # Display the board
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
    
    # Get and validate player input
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Choose an empty position between 0 and 8.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 8.")
    
    board[move] = "O"  # Player's move
    
    # Computer's turn
    if winner(board) is None:
        best_move = max((minimax(board[:i] + ["X"] + board[i+1:], False), i) for i in range(9) if board[i] == " ")[1]
        board[best_move] = "X"

# Display the final board and result
for i in range(0, 9, 3):
    print(" | ".join(board[i:i+3]))
result = winner(board)
print("Game Over! You", "Win!" if result == -10 else "Lose!" if result == 10 else "Draw!")