# Function to check if placing a queen at board[row][col] is safe
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:  # Check row on left side
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:  # Check upper diagonal on left side
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:  # Check lower diagonal on left side
            return False
    return True

# Function to solve the N Queens problem using backtracking
def solve_queens(board, col):
    if col >= len(board):  # All queens are placed
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):  # Check if it's safe to place queen
            board[i][col] = 1  # Place queen
            if solve_queens(board, col + 1):  # Recur to place rest of the queens
                return True
            board[i][col] = 0  # Backtrack
    return False

# Function to print the board with queens
def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))

# Main function to solve the 8x8 Queens puzzle
def solve():
    N = 8  # Size of the chessboard
    board = [[0] * N for _ in range(N)]  # Initialize an 8x8 board with 0s
    if solve_queens(board, 0):
        print_board(board)
    else:
        print("No solution found")

# Call the main function
solve()
